import random
import string


class FuncionarioData:
    @staticmethod
    def gerar_nome():
        return 'Funcionario ' + ''.join(random.choices(string.ascii_letters, k=6))

    @staticmethod
    def gerar_cpf():
        return ''.join(random.choices('0123456789', k=11))

    @staticmethod
    def novo_funcionario_valido():
        return {
            'nome': FuncionarioData.gerar_nome(),
            'cpf': FuncionarioData.gerar_cpf(),
            'birth_day': '01011990',
            'rg': '1234567',
            'ca_number': '12345',
            'status': 'ativo'
        }

    @staticmethod
    def novo_funcionario_inativo():
        return {
            'nome': FuncionarioData.gerar_nome(),
            'cpf': FuncionarioData.gerar_cpf(),
            'birth_day': '04041991',
            'rg': '2468135',
            'ca_number': '54321',
            'status': 'inativo'
        }

    @staticmethod
    def novo_funcionario_atividade_02():
        funcionario = FuncionarioData.novo_funcionario_valido()
        funcionario['atividade'] = 'Ativid 02'
        return funcionario

    @staticmethod
    def novo_funcionario_sem_epi():
        funcionario = FuncionarioData.novo_funcionario_valido()
        funcionario['nao_usa_epi'] = True
        return funcionario

    @staticmethod
    def funcionario_editado():
        return {
            'nome': FuncionarioData.gerar_nome(),
            'cpf': FuncionarioData.gerar_cpf(),
            'birth_day': '02021992',
            'rg': '7654321',
            'ca_number': '98765'
        }
