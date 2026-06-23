# Automacao Python + Selenium + Behave

Projeto de automacao de testes E2E com foco no fluxo de cadastro de funcionarios.

## Entrega do teste tecnico

- Visao geral do projeto: este README
- Relatorio executivo: `RELATORIO_ENTREGA.md`
- Guia de publicacao: `PUBLISH_GITHUB.md`

## Estrutura

- `features/`: arquivos `.feature` com cenarios BDD
- `features/steps/`: implementacao dos passos
- `pages/`: Page Objects
- `utils/`: configuracao, browser factory, logger e massa de dados
- `evidencias/`: screenshots e logs de execucao

## Cenarios cobertos

- Cadastro de funcionario com dados validos
- Cadastro de funcionario ativo
- Cadastro de funcionario inativo
- Cadastro de funcionario com atividade 02
- Cadastro de funcionario sem uso de EPI
- Edicao de funcionario cadastrado

## Requisitos

- Python 3.10+
- Microsoft Edge instalado (navegador padrao desta entrega)
- Dependencias do projeto instaladas

## Instalacao

```bash
python -m pip install -r requirements.txt
```

## Execucao local (Windows / PowerShell)

```powershell
$env:BASE_URL='http://analista-teste.seatecnologia.com.br/'
$env:BROWSER='edge'
$env:EDGE_BINARY_PATH='C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
$env:HEADLESS='true'
$env:BROWSER_ZOOM='0.7'
python -m behave
```

## Variaveis de ambiente

- `BASE_URL`: URL base da aplicacao
- `BROWSER`: navegador (`edge` como padrao da entrega; `chrome` opcional)
- `HEADLESS`: `true` ou `false`
- `BROWSER_ZOOM`: zoom global do navegador (`1.0` = 100%, `0.7` = 70%)
- `CHROMEDRIVER_PATH`: caminho opcional para ChromeDriver
- `EDGEDRIVER_PATH`: caminho opcional para EdgeDriver
- `EDGE_BINARY_PATH`: caminho opcional para o executavel do Edge
- `SCREENSHOTS_DIR`: pasta para capturas de falha
- `WARNING_LOG_FILE`: caminho do arquivo de warnings

## Evidencias

- Screenshots de falha: `evidencias/*.png`
- Log geral dos hooks: `evidencias/behave.log`
- Warnings do fluxo: `evidencias/warnings.log`

## Observacao tecnica

Em execucao headless, o select de atividade pode nao refletir visualmente a troca para `Ativid 02` em algumas execucoes. Nesses casos, o warning e registrado no log sem bloquear a continuidade da suite.

## Publicacao no GitHub

Siga o passo a passo em `PUBLISH_GITHUB.md`.

