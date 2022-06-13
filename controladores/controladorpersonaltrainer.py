from TrabalhoPOO.entidades.personaltrainer import PersonalTrainer
from TrabalhoPOO.controladores.controladorsistema import ControladorSistema
from TrabalhoPOO.telas.telapersonaltrainer import TelaPersonalTrainer


class ControladorPersonalTrainer():
    def __init__(self, controlador_sistema):
        self.__tela_personal = TelaPersonalTrainer()
        self.__manter_tela = bool
        self.__controlador_sistema = controlador_sistema

    def alterar_personal(self, cpf: str, nome: str, login: str, senha: str, habilitacao: str):
        if isinstance(cpf, str) and isinstance(nome, str) and isinstance(login, str) and \
                isinstance(senha, str) and isinstance(habilitacao, str):
            print("O que você deseja alterar")
            print("1. CPF: 2. Nome: 3.Login: 4.Senha: 0.tela inicial")
            opcao = int(input())
            while opcao != 0:
                if opcao == 1:
                    print("alterar cpf:")
                    cpf = input()
                elif opcao == 2:
                    print("Alterar nome")
                    nome = input()
                elif opcao == 3:
                    print("alterar login:")
                    login = input()
                elif opcao == 4:
                    print("Alterar senha")
                    senha = input()
                elif opcao == 0:
                   self.abre_tela_inicial()
                else:
                    print("Digite o valor correto")
                    continue

    def consultar_personal(self, cpf: str, nome: str, login: str, senha: str):
        if isinstance(cpf, str) and isinstance(nome, str) and isinstance(login, str) and \
                isinstance(senha, str):
            pass

    def abre_tela_inicial(self):
        pass

    def retornar(self):
        pass

    def verificar_login_senha(self, login: str, senha: str):
        if isinstance(login, str) and isinstance(senha, str):

            return True
