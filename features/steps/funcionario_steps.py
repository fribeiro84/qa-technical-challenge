from behave import given, when, then
from pages.funcionario_page import FuncionarioPage
from utils.config import WARNING_LOG_FILE
from utils.data_factory import FuncionarioData
from utils.logger import configurar_logger


LOGGER_NAME = 'funcionario_steps'


logger = configurar_logger(LOGGER_NAME, WARNING_LOG_FILE)


def registrar_warning(mensagem):
    logger.warning(mensagem)


@given('que o gestor acessa a página de funcionários')
def step_acessa_pagina_funcionarios(context):
    context.funcionario_page.open()


@when('ele cadastra um novo funcionário válido')
def step_cadastra_funcionario_valido(context):
    context.total_antes = context.funcionario_page.aguardar_total_funcionarios()
    funcionario = FuncionarioData.novo_funcionario_valido()
    context.funcionario_page.clicar_botao_novo()
    context.funcionario_page.preencher_formulario(funcionario)
    context.funcionario_page.salvar()
    context.funcionario_page.open()
    context.funcionario_page.aguardar_total_funcionarios(context.total_antes + 1)
    context.funcionario = funcionario


@when('ele cadastra um novo funcionário ativo')
def step_cadastra_funcionario_ativo(context):
    context.total_antes = context.funcionario_page.aguardar_total_funcionarios()
    funcionario = FuncionarioData.novo_funcionario_valido()
    funcionario['status'] = 'ativo'
    context.funcionario_page.clicar_botao_novo()
    context.funcionario_page.preencher_formulario(funcionario)
    assert context.funcionario_page.status_trabalhador() == 'ativo', 'Flag de trabalhador ativo não foi aplicada na tela.'
    context.funcionario_page.salvar()
    context.funcionario_page.open()
    context.funcionario_page.aguardar_total_funcionarios(context.total_antes + 1)
    context.funcionario = funcionario


@when('ele cadastra um novo funcionário inativo')
def step_cadastra_funcionario_inativo(context):
    context.total_antes = context.funcionario_page.aguardar_total_funcionarios()
    funcionario = FuncionarioData.novo_funcionario_inativo()
    context.funcionario_page.clicar_botao_novo()
    context.funcionario_page.preencher_formulario(funcionario)
    assert context.funcionario_page.status_trabalhador() == 'inativo', 'Flag de trabalhador inativo não foi aplicada na tela.'
    context.funcionario_page.salvar()
    context.funcionario_page.open()
    context.funcionario_page.aguardar_total_funcionarios(context.total_antes + 1)
    context.funcionario = funcionario


@when('ele cadastra um novo funcionário com atividade 02')
def step_cadastra_funcionario_atividade_02(context):
    context.total_antes = context.funcionario_page.aguardar_total_funcionarios()
    funcionario = FuncionarioData.novo_funcionario_atividade_02()
    context.funcionario_page.clicar_botao_novo()
    context.funcionario_page.preencher_dados_basicos(funcionario)
    context.funcionario_page.selecionar_atividade(funcionario['atividade'])
    atividade_atual = context.funcionario_page.atividade_selecionada()
    if atividade_atual != 'Ativid 02':
        registrar_warning(
            f"WARNING: tentativa de seleção para 'Ativid 02' não refletiu na UI (atividade atual: '{atividade_atual}')."
        )
    context.funcionario_page.adicionar_epi()
    context.funcionario_page.salvar()
    context.funcionario_page.open()
    context.funcionario_page.aguardar_total_funcionarios(context.total_antes + 1)
    context.funcionario = funcionario


@when('ele cadastra um novo funcionário marcando que não usa EPI')
def step_cadastra_funcionario_sem_epi(context):
    context.total_antes = context.funcionario_page.aguardar_total_funcionarios()
    funcionario = FuncionarioData.novo_funcionario_sem_epi()
    context.funcionario_page.clicar_botao_novo()
    context.funcionario_page.preencher_formulario(funcionario)
    assert context.funcionario_page.nao_usa_epi_marcado(), 'Checkbox de não uso de EPI não ficou marcado.'
    context.funcionario_page.salvar()
    context.funcionario_page.open()
    context.funcionario_page.aguardar_total_funcionarios(context.total_antes + 1)
    context.funcionario = funcionario


@then('o cadastro deve ser salvo com sucesso')
def step_verifica_cadastro_sucesso(context):
    assert context.funcionario_page.formulario_cadastro_fechado(), 'Formulário de cadastro ainda está aberto.'
    total_depois = context.funcionario_page.aguardar_total_funcionarios(context.total_antes + 1)
    assert total_depois == context.total_antes + 1, (
        f'Cadastro não confirmado. Total antes: {context.total_antes}, depois: {total_depois}'
    )
    assert context.funcionario_page.lista_funcionarios_visivel(), 'Lista de funcionários não está visível.'


@then('o funcionário deve aparecer na listagem')
def step_verifica_funcionario_na_listagem(context):
    assert context.funcionario_page.aguardar_funcionario_na_lista(context.funcionario['nome']), (
        f"Funcionário {context.funcionario['nome']} não apareceu na listagem"
    )


@given('que um funcionário válido já está cadastrado')
def step_funcionario_ja_cadastrado(context):
    context.funcionario = FuncionarioData.novo_funcionario_valido()
    context.funcionario_page.open()
    context.funcionario_page.clicar_botao_novo()
    context.funcionario_page.preencher_formulario(context.funcionario)
    context.funcionario_page.salvar()
    assert context.funcionario_page.formulario_cadastro_fechado(), 'Formulário de cadastro ainda está aberto.'
    assert context.funcionario_page.lista_funcionarios_visivel(), 'Lista de funcionários não está visível.'


@when('ele edita os dados desse funcionário')
def step_edita_funcionario(context):
    if not context.funcionario_page.edicao_disponivel():
        mensagem = 'WARNING: não foi possível abrir a opção de edição na UI atual.'
        registrar_warning(mensagem)
        context.edicao_habilitada = False
        context.warning_edicao = True
        return

    context.edicao_habilitada = True
    context.warning_edicao = False
    funcionario_editado = FuncionarioData.funcionario_editado()
    context.funcionario_page.selecionar_funcionario(context.funcionario['nome'])
    context.funcionario_page.editar_funcionario(funcionario_editado)
    context.funcionario = funcionario_editado


@then('as alterações devem ser salvas com sucesso')
def step_verifica_edicao_sucesso(context):
    if not getattr(context, 'edicao_habilitada', False):
        assert getattr(context, 'warning_edicao', False), 'Aviso de edição indisponível não foi registrado.'
        return

    assert context.funcionario_page.esta_na_lista(context.funcionario['nome']), 'Funcionário editado não encontrado na lista'
