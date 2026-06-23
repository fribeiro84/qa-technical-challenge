from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re
import time
from pages.base_page import BasePage
from utils.config import BASE_URL


class FuncionarioPage(BasePage):
    URL = BASE_URL
    BTN_NOVO = (By.XPATH, "//button[contains(., 'Adicionar Funcion')]")
    INPUT_NOME = (By.NAME, 'name')
    INPUT_CPF = (By.NAME, 'cpf')
    INPUT_DATA_NASCIMENTO = (By.NAME, 'birthDay')
    INPUT_RG = (By.NAME, 'rg')
    INPUT_CA = (By.NAME, 'caNumber')
    SWITCH_STATUS = (By.CSS_SELECTOR, 'button.ant-switch')
    RADIO_MASCULINO = (By.XPATH, "//label[contains(.,'Masculino')]")
    COMBO_ATIVIDADE = (
        By.XPATH,
        "(//*[contains(normalize-space(.), 'Selecione a atividade:')]/following::*[contains(@class,'ant-select-selector')])[1]",
    )
    CHECKBOX_NAO_USA_EPI_LABEL = (
        By.XPATH,
        "//label[contains(@class, 'ant-checkbox-wrapper') and .//span[normalize-space(.)='O trabalhador não usa EPI.']]",
    )
    CHECKBOX_NAO_USA_EPI_INPUT = (
        By.XPATH,
        "(//label[contains(@class, 'ant-checkbox-wrapper') and .//span[normalize-space(.)='O trabalhador não usa EPI.']]//input[@type='checkbox'])[1]",
    )
    BTN_ADICIONAR_EPI = (By.XPATH, "//*[normalize-space(.)='Adicionar EPI']")
    BOTAO_SALVAR = (By.CSS_SELECTOR, 'button[type="submit"]')
    RESUMO_ATIVOS = (By.XPATH, "//*[contains(normalize-space(.), 'Ativos') and contains(normalize-space(.), '/')]")
    INPUT_NOME_CADASTRO = (By.NAME, 'name')
    HEADING_FUNCIONARIOS = (By.XPATH, "//*[contains(normalize-space(.), 'Funcionário(s)')]")
    CARD_ACTION_MENU = (By.CSS_SELECTOR, 'div.c-jyZWAy')

    def open(self):
        self.open_url(self.URL)

    def clicar_botao_novo(self):
        self.click(self.BTN_NOVO)

    def preencher_dados_basicos(self, funcionario):
        self.definir_status_trabalhador(funcionario.get('status', 'inativo'))
        self.type(self.INPUT_NOME, funcionario['nome'])
        self.type(self.INPUT_CPF, funcionario['cpf'])
        self.type(self.INPUT_DATA_NASCIMENTO, funcionario['birth_day'])
        self.type(self.INPUT_RG, funcionario['rg'])
        self.click(self.RADIO_MASCULINO)
        self.type(self.INPUT_CA, funcionario['ca_number'])

    def preencher_formulario(self, funcionario):
        self.preencher_dados_basicos(funcionario)
        if funcionario.get('atividade'):
            self.selecionar_atividade(funcionario['atividade'])
        if funcionario.get('nao_usa_epi'):
            self.marcar_nao_usa_epi()
        else:
            self.adicionar_epi()

    def adicionar_epi(self):
        self._click_via_js(self.BTN_ADICIONAR_EPI)

    def definir_status_trabalhador(self, status):
        status_normalizado = str(status).strip().lower()
        switch = self.find(self.SWITCH_STATUS)
        if status_normalizado == 'inativo' and switch.text.strip().lower() != 'inativo':
            self._click_via_js(self.SWITCH_STATUS)
        elif status_normalizado == 'ativo' and switch.text.strip().lower() != 'ativo':
            self._click_via_js(self.SWITCH_STATUS)

    def status_trabalhador(self):
        return self.find(self.SWITCH_STATUS).text.strip().lower()

    def selecionar_atividade(self, atividade):
        seletor = self.wait.until(EC.element_to_be_clickable(self.COMBO_ATIVIDADE))
        for _ in range(2):
            seletor.click()
            try:
                opcao = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, f"//*[@role='option' and normalize-space(.)='{atividade}']"))
                )
                self.driver.execute_script('arguments[0].click();', opcao)
                if self.atividade_selecionada() == atividade:
                    return
            except TimeoutException:
                continue

        campo = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//*[contains(normalize-space(.), 'Selecione a atividade:')]/following::input[@role='combobox'])[1]")
            )
        )
        campo.send_keys(Keys.CONTROL, 'a')
        campo.send_keys(atividade)
        campo.send_keys(Keys.ENTER)

    def atividade_selecionada(self):
        atividade = self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "(//*[contains(normalize-space(.), 'Selecione a atividade:')]/following::*[contains(@class,'ant-select-selection-item')])[1]",
                )
            )
        )
        return atividade.text.strip()

    def marcar_nao_usa_epi(self):
        checkbox = self.wait.until(EC.presence_of_element_located(self.CHECKBOX_NAO_USA_EPI_INPUT))
        if not checkbox.is_selected():
            label = self.wait.until(EC.element_to_be_clickable(self.CHECKBOX_NAO_USA_EPI_LABEL))
            self.driver.execute_script('arguments[0].click();', label)

    def nao_usa_epi_marcado(self):
        checkbox = self.wait.until(EC.presence_of_element_located(self.CHECKBOX_NAO_USA_EPI_INPUT))
        return checkbox.is_selected()

    def _click_via_js(self, locator):
        element = self.find(locator)
        self.driver.execute_script('arguments[0].click();', element)

    def salvar(self):
        self._click_via_js(self.BOTAO_SALVAR)

    def _extrair_total_funcionarios(self, texto):
        match = re.search(r'Ativos\s+\d+/(\d+)', texto)
        return int(match.group(1)) if match else None

    def aguardar_total_funcionarios(self, total_esperado=None, timeout=20):
        fim = time.time() + timeout
        ultimo_texto = ''
        while time.time() < fim:
            texto = self.driver.find_element(By.TAG_NAME, 'body').text
            ultimo_texto = texto
            total_atual = self._extrair_total_funcionarios(texto)
            if total_atual is None:
                time.sleep(0.5)
                continue

            if total_esperado is None or total_atual == total_esperado:
                return total_atual
            time.sleep(0.5)
        if total_esperado is None:
            raise AssertionError(f'Não foi possível interpretar o resumo de ativos: {ultimo_texto}')
        raise AssertionError(f'Não foi possível confirmar total {total_esperado}. Último texto: {ultimo_texto}')

    def obter_total_funcionarios(self):
        return self.aguardar_total_funcionarios()

    def formulario_cadastro_fechado(self):
        return len(self.driver.find_elements(*self.INPUT_NOME_CADASTRO)) == 0

    def lista_funcionarios_visivel(self):
        return len(self.driver.find_elements(*self.HEADING_FUNCIONARIOS)) > 0

    def esta_na_lista(self, nome):
        body_text = self.driver.find_element(By.TAG_NAME, 'body').text
        return nome in body_text

    def aguardar_funcionario_na_lista(self, nome, timeout=20):
        fim = time.time() + timeout
        ultimo_texto = ''
        while time.time() < fim:
            texto = self.driver.find_element(By.TAG_NAME, 'body').text
            ultimo_texto = texto
            if nome in texto:
                return True
            time.sleep(0.5)
        raise AssertionError(f'Funcionário {nome} não apareceu na listagem. Último texto: {ultimo_texto}')

    def edicao_disponivel(self):
        return len(self.driver.find_elements(*self.CARD_ACTION_MENU)) > 0

    def selecionar_funcionario(self, nome):
        raise NotImplementedError('Edição indisponível na versão atual da aplicação.')

    def editar_funcionario(self, funcionario):
        raise NotImplementedError('Edição indisponível na versão atual da aplicação.')
