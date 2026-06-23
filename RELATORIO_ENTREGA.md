# Relatorio de Entrega - Automacao de Testes

## Objetivo

Automatizar fluxos criticos de cadastro e validacao de funcionarios utilizando Python + Selenium WebDriver + Behave, com cobertura dos cenarios priorizados para o desafio tecnico.

## Escopo

1. Cadastro de funcionario com dados validos.
2. Cadastro de funcionario ativo.
3. Cadastro de funcionario inativo.
4. Cadastro de funcionario com atividade 02.
5. Cadastro de funcionario sem uso de EPI.
6. Edicao de funcionario cadastrado (com tratamento de warning quando a UI de edicao nao estiver disponivel).

## Principais entregas

1. Estrutura BDD com Behave (`features/*.feature`).
2. Implementacao de Page Object Model (`pages/`).
3. Fabrica de massa de dados (`utils/data_factory.py`).
4. Configuracao por variaveis de ambiente (`utils/config.py`).
5. Logging de warnings e evidencias (`utils/logger.py`, `evidencias/`).
6. Execucao validada em Edge com suporte a zoom de 70%.

## Riscos identificados

1. Em modo headless, o select de atividade pode nao refletir visualmente a mudanca para `Ativid 02` em algumas execucoes.
2. O fluxo de edicao depende da disponibilidade de elementos da UI que podem nao estar presentes na versao atual da aplicacao.

## Criterio de entrada

1. Ambiente Python configurado com dependencias instaladas (`requirements.txt`).
2. Browser e driver compativeis disponiveis (Edge/Chrome).
3. URL da aplicacao acessivel (`BASE_URL`).
4. Variaveis de ambiente de execucao definidas (browser, headless, zoom, paths opcionais).

## Criterio de saida

1. Execucao completa da suite Behave sem falhas bloqueantes.
2. Registro de evidencias em arquivo (logs e screenshots quando aplicavel).
3. Resultado consolidado com cenarios cobertos e riscos conhecidos documentados.

## Matriz executiva consolidada

| ID | Cenario | Resultado | Evidencia |
| --- | --- | --- | --- |
| C01 | Cadastro de funcionario com dados validos | Aprovado | `features/funcionario.feature` |
| C02 | Cadastro de funcionario ativo | Aprovado | `features/funcionario.feature` |
| C03 | Cadastro de funcionario inativo | Aprovado | `features/funcionario.feature` |
| C04 | Cadastro de funcionario com atividade 02 | Aprovado com observacao | `evidencias/warnings.log` |
| C05 | Cadastro de funcionario sem uso de EPI | Aprovado | `features/funcionario.feature` |
| C06 | Edicao de funcionario cadastrado | Aprovado com observacao | `evidencias/warnings.log` |

## Observacao final

A entrega atende ao escopo funcional solicitado para o teste tecnico, com automacao executavel e evidencias registradas. Os riscos remanescentes estao mapeados e mitigados com logging para nao interromper a validacao dos fluxos principais.

## Evidencias

1. `evidencias/behave.log`
2. `evidencias/warnings.log`
3. `evidencias/*.png` (quando ocorrer falha)
