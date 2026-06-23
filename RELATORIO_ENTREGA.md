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
2. Browser e driver compativeis disponiveis (Edge como padrao da entrega; Chrome opcional).
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

### Matriz de Cobertura por Área

| Área | Cobertura Principal | Tipo |
| --- | --- | --- |
| Cadastro | Fluxo básico com dados válidos | Funcional |
| Cadastro | Validação de status (Ativo/Inativo) | Funcional |
| Cadastro | Seleção de atividade específica | Funcional |
| Cadastro | Validação de marcar/desmarcar EPI | Funcional |
| Edição | Atualização de dados cadastrais | Funcional |

## Comparativo prototipo x aplicacao

Prototipo analisado: https://tinyurl.com/yl58hs4m (destino Figma)
Aplicacao analisada: http://analista-teste.seatecnologia.com.br/

| Area | Esperado no prototipo | Observado na aplicacao | Resultado |
| --- | --- | --- | --- |
| Fonte | Tipografia consistente do layout Figma | Aplicacao usa `Ubuntu, sans-serif` em titulos e campos | Parcialmente aderente |
| Cores | Paleta azul/cinza e contraste conforme prototipo | Paleta principal azul/cinza aderente; variacoes de contraste em labels e estados | Parcialmente aderente |
| Itens de topo | Sequencia de etapas com rotulos distintos (Item 1..Item 6) | Barra superior com 9 blocos repetindo `ITEM 1` | Divergente |
| Titulo do painel | Contexto de listagem de funcionarios | Em fluxo de cadastro aparece `Adicionar Funcionário`; na listagem `Funcionário(s)` | Parcialmente aderente |
| Navegacao lateral | Itens devem levar para telas/etapas (incluindo `Em breve` para pendencias) | Clique nos 6 icones laterais manteve a mesma tela; nao exibiu `Em breve` | Divergente |
| Menu de acoes (...) | Opcoes de editar/excluir por registro | Nao foram identificadas opcoes visiveis `Editar/Excluir` no fluxo exploratorio | Divergente |
| CPF | Validacao de CPF (regra de negocio) | Campo bloqueia tamanho < 11, mas aceita `11111111111` (sem validacao de digitos verificadores) | Divergente |
| Data | Validacao de data de nascimento coerente | Campo `type=date` exige formato valido, mas aceita data futura (`2099-01-01`) | Divergente |
| Persistencia | Salvar funcionario e refletir em listagem/total | Salvar com `nao usa EPI` fechou formulario e incrementou total de `56/108` para `56/109` | Aderente |
| Recuperacao | Recuperar funcionario salvo sem erro | Total incrementou, mas o nome salvo nao ficou imediatamente visivel na listagem atual (possivel filtro/paginacao) | Parcialmente aderente |
| Compatibilidade | Funcionamento nos principais navegadores | Smoke test OK em `chromium`, `firefox` e `webkit` (acesso e renderizacao inicial) | Aderente |

## Evidencias adicionais da comparacao

1. Capturas comparativas da sessao (prototipo Figma vs aplicacao em producao).
2. Validacao tecnica de estilo na aplicacao: titulo principal em `Ubuntu, sans-serif` e cor de fundo `rgb(79, 161, 193)`.
3. Navegacao lateral: 6 icones clicados sem transicao para conteudo `Em breve`.
4. Validacao CPF: `checkValidity=false` para `123` (tamanho insuficiente) e `checkValidity=true` para `11111111111`.
5. Validacao data: `checkValidity=true` para data futura `2099-01-01`.
6. Persistencia: apos salvar, resumo mudou de `Ativos 56/108` para `Ativos 56/109`.
7. Compatibilidade: script smoke com Playwright retornou `ok` para `chromium`, `firefox` e `webkit`.

## Diferencas em relacao ao que ja estava documentado

Ja documentado anteriormente:
1. Em modo headless, selecao de atividade 02 pode nao refletir visualmente na UI.
2. Fluxo de edicao pode ficar indisponivel na UI atual.

Novo nesta comparacao prototipo x aplicacao:
1. Divergencia na barra de etapas (itens repetidos `ITEM 1`).
2. Navegacao lateral sem redirecionamento para conteudo `Em breve`.
3. Ausencia de opcoes visiveis de editar/excluir no fluxo explorado.
4. Validacao de CPF aparentemente apenas por tamanho (sem regra de digitos verificadores).
5. Data de nascimento aceita data futura.
6. Recuperacao por nome nao imediata na listagem atual, apesar da persistencia no total.

## Observacao final

A entrega atende ao escopo funcional solicitado para o teste tecnico, com automacao executavel e evidencias registradas. Os riscos remanescentes estao mapeados e mitigados com logging para nao interromper a validacao dos fluxos principais.

## Evidencias

1. `evidencias/behave.log`
2. `evidencias/warnings.log`
3. `evidencias/*.png` (quando ocorrer falha)
