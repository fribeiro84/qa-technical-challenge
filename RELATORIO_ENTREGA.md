# Relatorio de Entrega - Automacao de Testes

## Objetivo

Automatizar fluxos criticos de cadastro de funcionarios com Python + Selenium WebDriver + Behave.

## Escopo implementado

1. Cadastro de funcionario com dados validos.
2. Cadastro de funcionario ativo.
3. Cadastro de funcionario inativo.
4. Cadastro de funcionario com atividade 02.
5. Cadastro de funcionario sem uso de EPI.
6. Edicao de funcionario cadastrado (com comportamento de warning quando a UI de edicao nao esta disponivel).

## Arquitetura aplicada

- BDD com Behave (`features/*.feature`).
- Page Object Model (`pages/`).
- Fabrica de massa de dados (`utils/data_factory.py`).
- Configuracao por variaveis de ambiente (`utils/config.py`).
- Logging de warnings e evidencias (`utils/logger.py`, `evidencias/`).

## Resultado da validacao

- Suite executada com sucesso no ambiente alvo.
- Total atual: 6 cenarios e 18 passos aprovados.

## Risco conhecido

- Em modo headless, o componente de select de atividade pode nao refletir visualmente a mudanca para `Ativid 02` em algumas execucoes.
- Mitigacao aplicada: registro de warning em arquivo sem interromper os demais fluxos.

## Evidencias

- `evidencias/behave.log`
- `evidencias/warnings.log`
- `evidencias/*.png` (quando ocorrer falha)
