# Automação de Testes com Python, Selenium e Behave

## Estrutura do projeto

- `features/` - arquivos `.feature` com cenários BDD
- `features/steps/` - definições de steps do Behave
- `pages/` - Page Objects para encapsular interações
- `utils/` - helpers para navegador e dados de teste
- `evidencias/` - captura de telas quando um cenário falhar

## Requisitos

- Python 3.10+
- Chrome instalado

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Como executar

```bash
set BASE_URL=http://analista-teste.seatecnologia.com.br/
set HEADLESS=false
python -m behave
```

## Variáveis de ambiente úteis

- `BASE_URL` - URL base da aplicação
- `HEADLESS` - execute em modo sem cabeça (`true`/`false`)
- `CHROMEDRIVER_PATH` - caminho absoluto para um ChromeDriver local, opcional
- `SCREENSHOTS_DIR` - pasta onde falhas são capturadas

## Observações

- O framework usa `WebDriverWait` para sincronização
- A URL da aplicação é configurável por `BASE_URL`
- O caminho de evidências é configurável por `SCREENSHOTS_DIR`
