# Evidências de OCR da ECE 146/2021

Este diretório preserva duas execuções de OCR sobre o PDF digitalizado da
Emenda Constitucional Estadual nº 146/2021:

- **original probatório:** `../../arquivos/sapl-emenda_146.pdf`;
- **transcrição autorada usada pelo repositório:**
  `../../transcricoes/sapl-emenda_146.md`.

Os resultados daqui são evidência intermediária. Não substituem o PDF original
nem a transcrição autorada: servem para reproduzir o reconhecimento, comparar
motores e auditar a limpeza feita depois do OCR.

## Unlimited-OCR

Executado em GPU Tesla T4 com `baidu/Unlimited-OCR`, revisão
`07dea832e22aefee32ad281d4b80551282e1c168`, processando as páginas
individualmente com `OCR_MAX_LENGTH=4096`.

- `unlimited-ocr-execution.ipynb` — notebook com código, ambiente e saída da
  execução;
- `unlimited-ocr-raw.md` — resultado bruto preservado;
- `unlimited-ocr-clean.md` — limpeza do resultado bruto, sem substituir a
  transcrição autorada.

## PaddleOCR

Executado em GPU Tesla T4 com Paddle 3.3.0 e PP-OCRv6.

- `paddleocr-execution.ipynb` — notebook com código, ambiente e saída;
- `paddleocr.md` — resultado reconhecido;
- `paddleocr-metrics.json` — tempos medidos por página nas passagens fria e
  quente.

Os notebooks são registros de execução em ambiente Colab: instalações,
imports tardios, saídas e dependências de GPU fazem parte da evidência. Por
isso ficam fora dos gates Ruff e `ty` aplicáveis ao código de produção.
