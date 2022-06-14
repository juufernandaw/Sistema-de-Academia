from TrabalhoPOO.entidades.personaltrainer import PersonalTrainer
from TrabalhoPOO.controladores.controladorsistema import ControladorSistema
from TrabalhoPOO.telas.telapersonaltrainer import TelaPersonalTrainer
from TrabalhoPOO.telas.telasistema import TelaSistema

class ControladorPersonalTrainer():
    def __init__(self, controlador_sistema):
        self.__tela_personal = TelaPersonalTrainer()
        self.__manter_tela = bool
        self.__controlador_sistema = controlador_sistema
        self.__tela_sistema = TelaSistema()
        self.__personal = PersonalTrainer(123456789, Judi Goilang, "Adm", "Adm", '01')
        #self.__dados_personal = {'cpf': "123456789", 'nome': "Judi Goilang", 'login': "Adm", 'senha': "Adm"", 'habilitacao': "01"}#instancia da classe

    def alterar_personal(self):
        alterar, opcao = self.__tela_sistema.mostrar_tela_alterar_dados() #get e setter modificando com isso
        switcher = {1: self.__personal.cpf, 2: self.__personal.nome, 3: self.__personal.login, 4: self.__personal.senha, 5: self.__personal.habilitacao}
        switcher[opcao]() = alterar #TESTAR ESSA loucura

    def consultar_personal(self, cpf: str, nome: str, login: str, senha: str):
        if isinstance(cpf, str) and isinstance(nome, str) and isinstance(login, str) and \
                isinstance(senha, str):
            pass           
            
    def abre_tela_inicial(self):
        pass

    def retornar(self):
        pass

    def verificar_login_senha(): #VERIFICAR 
        login, senha = self.__tela_sistema.logar()
        if isinstance(login, str) and isinstance(senha, str):
            if self.__personal.login == login and self.__personal.senha == senha:
                return True
        
