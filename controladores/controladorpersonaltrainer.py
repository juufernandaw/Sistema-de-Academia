from TrabalhoPOO.entidades.personaltrainer import PersonalTrainer
from TrabalhoPOO.controladores.controladorsistema import ControladorSistema
from TrabalhoPOO.telas.telapersonaltrainer import TelaPersonalTrainer
from TrabalhoPOO.telas.telasistema import TelaSistema
from TrabalhoPOO.telas.telaaluno import TelaAluno


class ControladorPersonalTrainer():
    def __init__(self, controlador_sistema):
        self.__tela_personal = TelaPersonalTrainer()
        self.__tela_aluno = TelaAluno()
        self.__manter_tela = bool
        self.__controlador_sistema = controlador_sistema
        self.__tela_sistema = TelaSistema()
        self.__personal = PersonalTrainer("12345678905", "Judi", "Adm", "Adm", "01" ) #criou o personal

    def verificar_login_senha(self, login, senha):  # VERIFICAR o login e senha.
        if isinstance(login, str) and isinstance(senha, str):
            if self.__personal.senha == login and self.__personal.senha == senha: #Set Para Mudar
                return True

    def alterar_personal(self):#aqui ele está alterando os dados do personal baseado no dicionario da tela
        cpf = self.__tela_personal.mexer_personal()
        if self.__personal is not None:
            novos_dados = self.__tela_personal.tela_alterar_dados()
            self.__personal.nome = novos_dados["nome"]
            self.__personal.cpf = novos_dados["cpf"]
            self.__personal.login = novos_dados["login"]
            self.__personal.senha = novos_dados["senha"]
            self.__personal.habilitacao = novos_dados["habilitacao"]
        else:
            print("Dados não alterados")

    def tela_alterar_dados_alunos(self):
        if self.__tela_personal.mexer_personal() == 2:
            self.__tela_aluno.mexer_aluno()

    @property
    def consultar_personal(self):
        return self.__personal
            
    def abre_tela_inicial(self):
        self.__tela_sistema.mostrar_tela_personal()

    def retornar(self):
        pass


