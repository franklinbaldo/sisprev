"""P4 — reading the provisions a regra's ``fundamentacao*`` cites, in prose.

RFC 0001's P4 says the prose is for humans and the frontmatter is for checks:
``dispositivos:`` is the canonical, machine-checkable link, while
``FUNDAMENTACAO*`` stays free text. This module is the bridge between the
two — it reads the prose and reports **what it claims to cite**, so the gap
between "what the regra says it is founded on" and "what it declares in
``dispositivos:``" becomes a measured number instead of an invisible hole.

It **reports, never concludes** (princípio da autoria humana). Nothing here
writes a link: deciding that a regra is founded on a given provision is a
legal judgment, and this module's own output is the evidence an auditor
weighs, not a verdict. That distinction is not ceremony — the prose in this
corpus is genuinely ambiguous in ways no parser resolves:

- the owning norm is sometimes only implied ("artigo 40, §§ 3º e 8º com
  redação dada pela EC 41/2003" names the *amending* norm, never the CF);
- the same norm appears under many spellings — ``nº``/``n.``/``EC``, with
  and without "Estadual", ``41/2003`` and ``41/03`` — which is exactly the
  E6 the RFC diagnoses;
- citations reach *inside* a provision ("inciso III, **segunda parte**"),
  naming a fragment the dispositivo schema deliberately cannot address.

So every extracted citation carries a ``situacao`` saying how far it could
be resolved, and the unresolvable ones are reported as such rather than
rounded to the nearest addressable thing.

**Known under-reading**: an inciso *range* ("34, I a III") yields only its
first inciso. Under-reporting a citation leaves work visible in the queue;
inventing the intermediate incisos would put provisions in a regra's record
that its prose never named, so the bias is deliberate.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from enum import StrEnum

from dispositivo_endereco import Componente, TipoComponente, slug_do_endereco, validar_aninhamento
from pydantic import ValidationError

# Norm spellings observed in the corpus -> the P4 vocabulary key. Ordered
# most-specific first: "Emenda Constitucional Estadual nº 146/2021" must not
# be read as "Emenda Constitucional" plus noise.
#
# This table is a *reading aid for prose*, not a second vocabulary: the key
# it produces is resolved against the authored norma.md docs by the caller,
# so a spelling that maps to an unauthored key is reported, never trusted.
_N = r"n?[.ºo°]*\s*"
NORMA_PADROES: tuple[tuple[str, str], ...] = (
    (rf"Emenda\s+[àa]\s+Constitui[çc][ãa]o\s+Estadual\s+(?:{_N})?146/2021", "ece-146-2021"),
    (rf"Emenda\s+Constitucional\s+Estadual\s+(?:{_N})?146/2021", "ece-146-2021"),
    (rf"EC\s*E?\s*(?:{_N})?146/(?:2021|21)", "ece-146-2021"),
    (rf"Emenda\s+Constitucional\s+(?:{_N})?20/1998", "ec-20-1998"),
    (rf"EC\s+(?:{_N})?20/(?:1998|98)", "ec-20-1998"),
    (rf"Emenda\s+Constitucional\s+(?:{_N})?41/(?:2003|03)", "ec-41-2003"),
    (rf"EC\s+(?:{_N})?41/(?:2003|03)", "ec-41-2003"),
    (rf"Emenda\s+Constitucional\s+(?:{_N})?47/2005", "ec-47-2005"),
    (rf"EC\s+(?:{_N})?47/(?:2005|05)", "ec-47-2005"),
    (rf"Emenda\s+Constitucional\s+(?:{_N})?70/2012", "ec-70-2012"),
    (rf"EC\s+(?:{_N})?70/(?:2012|12)", "ec-70-2012"),
    (rf"Emenda\s+Constitucional\s+(?:{_N})?88/2015", "ec-88-2015"),
    (rf"EC\s+(?:{_N})?88/(?:2015|15)", "ec-88-2015"),
    (rf"Emenda\s+Constitucional\s+(?:{_N})?103/2019", "ec-103-2019"),
    (rf"EC\s+(?:{_N})?103/(?:2019|19)", "ec-103-2019"),
    (rf"Lei\s+Complementar\s+(?:Estadual\s+)?(?:{_N})?1\.?100/2021", "lce-1100-2021"),
    (rf"LC\s*E?\s*(?:{_N})?1\.?100/(?:2021|21)", "lce-1100-2021"),
    (rf"Lei\s+Complementar\s+(?:Estadual\s+)?(?:{_N})?432/2008", "lce-432-2008"),
    (rf"LC\s*E?\s*(?:{_N})?432/(?:2008|08)", "lce-432-2008"),
    (rf"Lei\s+Complementar\s+(?:Estadual\s+)?(?:{_N})?949/2017", "lce-949-2017"),
    (rf"Lei\s+Complementar\s+(?:{_N})?51/1985", "lc-51-1985"),
    (rf"LC\s+(?:{_N})?51/(?:1985|85)", "lc-51-1985"),
    (rf"Lei\s+Complementar\s+(?:{_N})?152/2015", "lc-152-2015"),
    (rf"Lei\s+(?:{_N})?10\.?887/2004", "lei-10887-2004"),
    (r"Constitui[çc][ãa]o\s+Federal", "cf88"),
    (r"\bCF\b(?:\s*/\s*88)?", "cf88"),
)
_NORMA_RE = re.compile("|".join(f"(?P<n{i}>{p})" for i, (p, _) in enumerate(NORMA_PADROES)), re.IGNORECASE)

# A norm named right after "com (a) redação dada por/pela" is the *amending*
# norm — the wording — never the norm the provision belongs to. Getting this
# backwards is the single most likely way to attribute an article to the
# wrong norm, so it is a rule rather than a heuristic over distance.
_REDACAO_ANTES = re.compile(
    r"com\s+(?:a\s+)?reda[çc][ãa]o\s+(?:dada\s+)?(?:pel[ao]|de|d[oa])\s*$", re.IGNORECASE
)

# Names a clause *inside* a provision. The citation still resolves to the
# provision — see Citacao.qualificador for why — but the narrowing is kept so
# it stays visible in reports.
_FRAGMENTO = re.compile(r"(?:primeira|segunda|terceira)\s+parte|parte\s+final", re.IGNORECASE)

_ART = re.compile(r"\bartigos?\s*(\d+)\s*[º°]?(?:\s*-\s*([A-Z]))?", re.IGNORECASE)
# A bare number continuing an enumeration: "artigos 17, 20, 45 e 62" and
# "§§ 2º e 3º" both spell their level only once. Excludes anything glued to a
# word or a slash, so a norm's own digits (146/2021) are never read as an
# article.
_NUMERO_NU = re.compile(r"(?<![\w/.])(\d+)\s*[º°]?(?:\s*-\s*([A-Z]))?(?![\w/])")
_PAR = re.compile(r"§§?\s*(\d+)\s*[º°]?(?:\s*-\s*([A-Z]))?")
_INC = re.compile(r"\binciso\s+([IVXLC]+)\b", re.IGNORECASE)
_ALI = re.compile(r"\bal[íi]nea\s+[\"'“]?([a-z])[\"'”]?", re.IGNORECASE)
_CAPUT = re.compile(r"\bcaput\b", re.IGNORECASE)
# A bare Roman numeral inside an enumeration ("artigos 25, 27, I; 33") is an
# inciso of the article that precedes it.
_INC_NU = re.compile(r"(?<=[,;]\s)([IVXLC]+)(?=[,;.\s]|$)")
# The separator immediately before an enumerated item, when it is a ";" —
# see _tokens_de_enumeracao for why that decides the level.
_SEPARADOR_ARTIGO = re.compile(r";\s*(?:e\s+)?$")

_TOKEN_PROXIMO = 3

# (posição, nível, (valor, sufixo)) — um marcador de endereço lido da prosa.
_Token = tuple[int, str, tuple[str | None, str | None]]
# Endereço em construção: nível -> (valor, sufixo), antes de virar Componente.
_Endereco = dict[str, tuple[str | None, str | None]]


class SituacaoCitacao(StrEnum):
    """How far a prose citation could be resolved — never a verdict on the regra."""

    ENDERECAVEL = "enderecavel"
    """Owning norm identified and the address parses — resolvable against the bundle."""

    SEM_NORMA = "sem_norma"
    """An article whose owning norm the prose never names (only the amending one)."""

    ENDERECO_INVALIDO = "endereco_invalido"
    """The parsed components don't form a legal address — reported, never raised."""


@dataclass(frozen=True)
class Citacao:
    """One provision a fundamentação claims to cite, as read from the prose."""

    situacao: SituacaoCitacao
    norma: str | None
    componentes: tuple[Componente, ...]
    redacao: str | None
    """Amending norm named by the prose ("com redação dada pela EC 41/2003"), if any."""
    trecho: str
    """The prose span this was read from — so a human can check the reading."""
    qualificador: str | None = None
    """A clause the prose narrows the provision to ("segunda parte"), when present.

    The citation still resolves to the whole provision: in this corpus the
    qualifier names a *clause inside one provision*, not another provision.
    CF art. 40, § 1º, III (EC 103/2019) has no alíneas — its "segunda parte"
    is the "no âmbito dos Estados, do Distrito Federal e dos Municípios"
    clause of the same inciso, which is precisely the one that reaches a
    State regime. Transcribing it as a separate dispositivo would invent a
    unit the norm does not have, and dropping the citation would leave the
    catalog's most-cited provision permanently outside the P4 check.

    So the split follows P4's own division of labour: the frontmatter answers
    *which provision*, the prose answers *which clause of it*. Kept here so
    the narrowing is visible in reports rather than silently discarded — the
    resolution the frontmatter does not carry is a real, stated cost.
    """

    @property
    def endereco_id(self) -> str | None:
        """Return ``<norma>/<endereço>``, or None when it isn't addressable."""
        if self.situacao is not SituacaoCitacao.ENDERECAVEL or self.norma is None:
            return None
        return f"{self.norma}/{slug_do_endereco(self.componentes)}"


def _mencoes(texto: str) -> list[tuple[int, int, str, bool]]:
    """Return ``(inicio, fim, chave, e_redacao)`` for every norm named in ``texto``."""
    encontradas = []
    for m in _NORMA_RE.finditer(texto):
        chave = next(c for i, (_, c) in enumerate(NORMA_PADROES) if m.group(f"n{i}"))
        e_redacao = _REDACAO_ANTES.search(texto[max(0, m.start() - 40) : m.start()]) is not None
        encontradas.append((m.start(), m.end(), chave, e_redacao))
    return encontradas


def _clausulas(texto: str) -> tuple[list[tuple[str, str, str | None]], list[str]]:
    """Split prose into ``(trecho de artigos, norma dona, redação)`` clauses.

    Also returns the spans that hold articles with no owning norm after them
    — the "artigo 40, §§ 3º e 8º com redação dada pela EC 41/2003" case,
    where attributing the article to the nearest named norm would attribute
    it to the amendment.
    """
    mencoes = _mencoes(texto)
    clausulas: list[tuple[str, str, str | None]] = []
    orfaos: list[str] = []
    cursor = 0
    for i, (inicio, fim, chave, e_redacao) in enumerate(mencoes):
        if e_redacao:
            # A wording marker owns nothing. Anything still pending before it
            # has no owning norm named at all.
            pendente = texto[cursor:inicio]
            if _ART.search(pendente):
                orfaos.append(pendente.strip())
                cursor = fim
            continue
        redacao = mencoes[i + 1][2] if i + 1 < len(mencoes) and mencoes[i + 1][3] else None
        clausulas.append((texto[cursor:inicio], chave, redacao))
        cursor = mencoes[i + 1][1] if redacao else fim
    restante = texto[cursor:]
    if _ART.search(restante):
        orfaos.append(restante.strip())
    return clausulas, orfaos


def _tokens_tipados(trecho: str) -> tuple[list[_Token], list[tuple[int, int]]]:
    """Collect the tokens that spell their own level, plus the spans they occupy."""
    achados: list[_Token] = []
    ocupado: list[tuple[int, int]] = []
    # artigo/parágrafo carry an optional suffix ("6º-A", "§ 4º-B"); inciso and
    # alínea never do, so their patterns have a single group.
    for regex, tipo in ((_ART, "artigo"), (_PAR, "paragrafo")):
        for m in regex.finditer(trecho):
            achados.append((m.start(), tipo, (m.group(1), m.group(2))))
            ocupado.append((m.start(), m.end()))
    for regex, tipo in ((_INC, "inciso"), (_ALI, "alinea")):
        for m in regex.finditer(trecho):
            achados.append((m.start(), tipo, (m.group(1), None)))
            ocupado.append((m.start(), m.end()))
    for m in _CAPUT.finditer(trecho):
        achados.append((m.start(), "caput", (None, None)))
        ocupado.append((m.start(), m.end()))
    return achados, ocupado


def _tokens_de_enumeracao(trecho: str, tipados: list[_Token], ocupado: list[tuple[int, int]]) -> list[_Token]:
    """Collect the bare items continuing an enumeration, taking their level from it.

    An enumeration spells its level once: "artigos 17, 20, caput, 45 e 62"
    and "§§ 2º e 3º" both continue with bare numbers. Each such number takes
    the level of the nearest *typed* marker before it, so the list survives
    non-numeric items in the middle — stopping at the first of those was a
    real bug, which made "caput" attach to art. 17 instead of art. 20.
    """
    achados: list[_Token] = []
    niveis = sorted((pos, tipo) for pos, tipo, _ in tipados if tipo in {"artigo", "paragrafo"})
    tem_artigo = any(tipo == "artigo" for _, tipo in niveis)
    for m in _NUMERO_NU.finditer(trecho):
        if any(inicio <= m.start() < fim for inicio, fim in ocupado):
            continue
        anteriores = [tipo for pos, tipo in niveis if pos < m.start()]
        if not anteriores:
            continue
        # The separator disambiguates the level. In this corpus ';' separates
        # *articles* while ',' and 'e' continue whatever is being enumerated:
        # "artigos 10, I; 28, I; 31, §§ 1º e 2º; 32, I e II" — without this,
        # every number after the first '§' inherited "paragrafo", inventing a
        # "§ 62 do art. 31" out of what is plainly article 62.
        pontovirgula = _SEPARADOR_ARTIGO.search(trecho[: m.start()]) is not None
        nivel = "artigo" if (pontovirgula and tem_artigo) else anteriores[-1]
        achados.append((m.start(), nivel, (m.group(1), m.group(2))))

    for m in _INC_NU.finditer(trecho):
        proximos = tipados + achados
        if not any(abs(m.start() - pos) < _TOKEN_PROXIMO for pos, _, _ in proximos):
            achados.append((m.start(), "inciso", (m.group(1), None)))
    return achados


def _tokens(trecho: str) -> list[_Token]:
    """Collect every address token in a clause, in reading order."""
    tipados, ocupado = _tokens_tipados(trecho)
    achados = tipados + _tokens_de_enumeracao(trecho, tipados, ocupado)
    achados.sort()
    return achados


def _componentes(bruto: _Endereco) -> tuple[Componente, ...] | None:
    """Build validated Componentes from a raw address, or None if they don't validate.

    Returning None instead of raising keeps this module inside the project's
    "report, never raise" contract: prose that reads as an impossible address
    becomes an ``ENDERECO_INVALIDO`` citation the auditor can see.
    """
    ordem = ("artigo", "paragrafo", "caput", "inciso", "alinea")
    try:
        componentes = tuple(
            Componente(
                tipo=TipoComponente(nivel),
                valor=bruto[nivel][0],
                sufixo=bruto[nivel][1],
            )
            for nivel in ordem
            if nivel in bruto
        )
    except (ValidationError, ValueError):
        return None
    return componentes if not validar_aninhamento(componentes) else None


def _aplicar(enderecos: list[_Endereco], atual: _Endereco, tipo: str, valores: tuple) -> _Endereco:
    """Add one non-artigo token to the address being built, closing it if the level repeats.

    A repeated level means the prose moved on to a sibling provision ("§ 6º,
    I, e § 7º, I"), so the address so far is emitted and a new one starts from
    the levels that still apply.
    """
    if tipo == "paragrafo":
        if {"paragrafo", "inciso", "caput"} & atual.keys():
            enderecos.append(atual)
            atual = {"artigo": atual["artigo"]}
        atual["paragrafo"] = valores
    elif tipo == "inciso":
        if "inciso" in atual:
            enderecos.append(atual)
            atual = {k: v for k, v in atual.items() if k in {"artigo", "paragrafo"}}
        atual["inciso"] = (valores[0], None)
    elif tipo == "alinea":
        atual["alinea"] = ((valores[0] or "").lower(), None)
    else:  # caput
        atual["caput"] = (None, None)
    return atual


def _enderecos(trecho: str) -> list[_Endereco]:
    """Walk a clause's tokens, emitting one raw address per provision cited."""
    enderecos: list[_Endereco] = []
    atual: _Endereco = {}
    for _, tipo, valores in _tokens(trecho):
        if tipo == "artigo":
            if atual:
                enderecos.append(atual)
            atual = {"artigo": valores}
        elif atual:
            # A qualifier before any article names nothing, so it is dropped.
            atual = _aplicar(enderecos, atual, tipo, valores)
    if atual:
        enderecos.append(atual)
    return enderecos


def extrair_citacoes(texto: str) -> list[Citacao]:
    """Read every provision a fundamentação claims to cite, with how far it resolved."""
    if not texto.strip():
        return []

    citacoes: list[Citacao] = []
    clausulas, orfaos = _clausulas(texto)

    for trecho, norma, redacao in clausulas:
        achado = _FRAGMENTO.search(trecho)
        qualificador = achado.group(0).strip().lower() if achado else None
        for bruto in _enderecos(trecho):
            componentes = _componentes(bruto)
            if componentes is None:
                situacao = SituacaoCitacao.ENDERECO_INVALIDO
                componentes = ()
            else:
                situacao = SituacaoCitacao.ENDERECAVEL
            citacoes.append(
                Citacao(
                    situacao=situacao,
                    norma=norma,
                    componentes=componentes,
                    redacao=redacao,
                    trecho=trecho.strip(),
                    qualificador=qualificador,
                )
            )

    for trecho in orfaos:
        for bruto in _enderecos(trecho):
            componentes = _componentes(bruto) or ()
            citacoes.append(
                Citacao(
                    situacao=SituacaoCitacao.SEM_NORMA,
                    norma=None,
                    componentes=componentes,
                    redacao=None,
                    trecho=trecho,
                )
            )
    return citacoes
