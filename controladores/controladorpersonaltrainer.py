from TrabalhoPOO.entidades.personaltrainer import PersonalTrainer
from TrabalhoPOO.telas.telapersonaltrainer import TelaPersonalTrainer
from TrabalhoPOO.telas.telasistema import TelaSistema
from TrabalhoPOO.telas.telaaluno import TelaAluno
from TrabalhoPOO.controladores.controladoraluno import ControladorAluno


class ControladorPersonalTrainer():
    def __init__(self, controlador_sistema):
        self.__tela_personal = TelaPersonalTrainer()
        self.__tela_aluno = TelaAluno()
        self.__tela_sistema = TelaSistema()
        self.__manter_tela = bool
        self.__controlador_sistema = controlador_sistema
        self.__aluno = ControladorAluno(self.__controlador_sistema)  # VERIFICAR ISSO AQUI COM O PROFESSOR
        self.__personal = PersonalTrainer("12345678905", "Judi", "Adm", "Adm", "01")  # criou o personal

    def verificar_login_senha(self, login, senha):  # VERIFICAR o login e senha.
        if isinstance(login, str) and isinstance(senha, str):
            if self.__personal.senha == login and self.__personal.senha == senha:  # Set Para Mudar
                return True

    def alterar_personal(self):  # aqui ele está alterando os dados do personal baseado no dicionario da tela
        if self.__personal is not None:
            novos_dados = self.__tela_personal.tela_alterar_dados()
            self.__personal.nome = novos_dados["nome"]
            self.__personal.cpf = novos_dados["habilitacao"]
            self.__personal.login = novos_dados["login"]
            self.__personal.senha = novos_dados["senha"]
            self.__personal.habilitacao = novos_dados["habilitacao"]
        else:
            print("Dados não alterados")

    def tela_alterar_dados_alunos(self):
        if self.__tela_personal.mexer_personal() == 2:  # na tela personal tem a opcao do personal escolher
            self.__tela_aluno.mexer_aluno()  # mostrar as opcoes q está na tela aluno q o prof acessa.
            while True:  # aqui ele vai fazer o laço e verificar a opcao do mexer alu.
                if self.__tela_aluno.mexer_aluno() == 1:
                    self.__aluno.incluir_aluno()
                elif self.__tela_aluno.mexer_aluno() == 2:
                    self.__aluno.alterar_aluno()
                elif self.__tela_aluno.mexer_aluno() == 3:
                    self.__aluno.excluir_aluno()
                elif self.__tela_aluno.mexer_aluno() == 4:
                    self.__aluno.listar_alunos()
                elif self.__tela_aluno.mexer_aluno() == 5:  # Duvida aqui o consultar! COMO fazer? se precisa do cpf
                    self.__aluno.consultar_aluno("aqui seria o CPF")
                elif self.__tela_aluno.mexer_aluno() == 6:
                    self.__aluno.retornar()
                else:
                    print("opcao de escolha invalida")
                    self.tela_alterar_dados_alunos()  # Pode fazer isso? Para voltar ao método

    @property
    def consultar_personal(self):
        return self.__personal

    def abre_tela_inicial(self):  # abre a tela personal pos login da tela do sistema
        self.__tela_sistema.mostrar_tela_personal()

    def retornar(self):
        pass
