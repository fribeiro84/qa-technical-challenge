# language: pt
Funcionalidade: Gerenciamento de funcionários
  Como analista de QA
  Quero cadastrar e editar funcionários
  Para validar os principais fluxos da aplicação

  Cenário: Cadastro de funcionário com dados válidos
    Dado que o gestor acessa a página de funcionários
    Quando ele cadastra um novo funcionário válido
    Então o cadastro deve ser salvo com sucesso

  Cenário: Cadastro de funcionário ativo
    Dado que o gestor acessa a página de funcionários
    Quando ele cadastra um novo funcionário ativo
    Então o cadastro deve ser salvo com sucesso

  Cenário: Cadastro de funcionário inativo
    Dado que o gestor acessa a página de funcionários
    Quando ele cadastra um novo funcionário inativo
    Então o cadastro deve ser salvo com sucesso

  Cenário: Cadastro de funcionário com atividade 02
    Dado que o gestor acessa a página de funcionários
    Quando ele cadastra um novo funcionário com atividade 02
    Então o cadastro deve ser salvo com sucesso

  Cenário: Cadastro de funcionário sem uso de EPI
    Dado que o gestor acessa a página de funcionários
    Quando ele cadastra um novo funcionário marcando que não usa EPI
    Então o cadastro deve ser salvo com sucesso

  Cenário: Edição de funcionário cadastrado
    Dado que um funcionário válido já está cadastrado
    Quando ele edita os dados desse funcionário
    Então as alterações devem ser salvas com sucesso
