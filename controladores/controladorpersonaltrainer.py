from TrabalhoPOO.entidades.personaltrainer import PersonalTrainer
from TrabalhoPOO.controladores.controladorsistema import ControladorSistema
from TrabalhoPOO.telas.telapersonaltrainer import TelaPersonalTrainer


class ControladorPersonalTrainer():
    def __init__(self, controlador_sistema):
        self.__tela_personal = TelaPersonalTrainer()
        self.__manter_tela = bool
        self.__controlador_sistema = controlador_sistema

    def alterar_personal(self, cpf: str, nome: str, login: str, senha: str):
        if isinstance(cpf, str) and isinstance(nome, str) and isinstance(login, str) and \
                isinstance(senha, str):
            pass

    def consultar_personal(self, cpf: str, nome: str, login: str, senha: str):
        if isinstance(cpf, str) and isinstance(nome, str) and isinstance(login, str) and \
                isinstance(senha, str):
            pass

    def abre_tela_inicial(self):
        pass

    def retornar(self):
        pass

    def logar(self, login: str, senha: str):
        if isinstance(login, str) and isinstance(senha, str):
            pass
