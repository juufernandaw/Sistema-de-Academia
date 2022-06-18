from TrabalhoPOO.entidades.personaltrainer import PersonalTrainer
from TrabalhoPOO.telas.telapersonaltrainer import TelaPersonalTrainer
from TrabalhoPOO.telas.telasistema import TelaSistema
from TrabalhoPOO.telas.telaaluno import TelaAluno
# from TrabalhoPOO.controladores.controladortreinodiario import TreinoDiario
# from TrabalhoPOO.controladores.controladorsistema import ControladorSistema


class ControladorPersonalTrainer():
    def __init__(self, controlador_sistema):
        self.__tela_personal = TelaPersonalTrainer()
        self.__tela_aluno = TelaAluno()
        self.__tela_sistema = TelaSistema()
        self.__manter_tela = bool
        self.__controlador_sistema = controlador_sistema
        self.__personal = PersonalTrainer("12345678905", "Judi", "Adm", "Adm", "01")  # criou o personal

    def verificar_login_senha(self, login, senha):  # VERIFICAR o login e senha.
        if isinstance(login, str) and isinstance(senha, str):
            if self.__personal.senha == login and self.__personal.senha == senha:  # Set Para Mudar
                return True

    def abre_tela_inicial(self):  # abre a tela personal pos login da tela do sistema
        self.__tela_personal.mexer_personal()
        mexer_personal_opcoes = {1: self.alterar_personal,
                                 2: self.tela_alterar__dados_alunos
                                 }
        while True:
            opcao_escolhida = self.__tela_personal.mexer_personal()
            if opcao_escolhida == 0:
                return self.retornar(0)
            else:
                funcao_escolhida = mexer_personal_opcoes[opcao_escolhida]
            return funcao_escolhida()

    def alterar_personal(self):  # aqui ele está alterando os dados do personal baseado no dicionario da tela
        self.__tela_personal.tela_alterar_dados()
        if self.__personal is not None:
            novos_dados = self.__tela_personal.tela_alterar_dados()  # vai ser um dicionario
            self.__personal.nome = novos_dados["nome"]
            self.__personal.cpf = novos_dados["habilitacao"]
            self.__personal.login = novos_dados["login"]
            self.__personal.senha = novos_dados["senha"]
            self.__personal.habilitacao = novos_dados["habilitacao"]

        return self.voltar_ao_menu_personal()

    def tela_alterar__dados_alunos(self):  # abre_tela_inicial manda para ca
        self.__tela_aluno.mexer_aluno()  # na tela personal tem a opcao do personal escolher
        mexer_personal_opcoes = {1: self.__controlador_sistema.controladoraluno.incluir_aluno,
                                 2: self.__controlador_sistema.controladoraluno.alterar_aluno,
                                 3: self.__controlador_sistema.controladoraluno.excluir_aluno,
                                 4: self.__controlador_sistema.controladoraluno.listar_alunos,
                                 5: self.__controlador_sistema.controladoraluno.consultar_aluno,
                                 6: self.voltar_ao_menu_personal,
                                 7: self.consultar_tela_desempenho}
        while True:
            opcao_modificar_aluno = self.__tela_aluno.mexer_aluno()
            funcao_escolhida = mexer_personal_opcoes[opcao_modificar_aluno]
            return funcao_escolhida()

    def consultar_tela_desempenho(self):  # NAO TEM A OPCAO NA LISTA DE MEXER ALUNO!
        return self.__controlador_sistema.controlador_treino_diario.mostrar_tela_treino_diario()

    def consultar_desempenho(self):
        escolha = self.consultar_tela_desempenho()

    def alterar_treino_aluno(self):
        pass

    @property
    def consultar_personal(self):
        return self.__personal

    def voltar_ao_menu_personal(self):
        return self.__tela_personal.mexer_personal()

    def retornar(self, opcao_escolhida):
        return self.__tela_sistema.logar(opcao_escolhida)


# if self.__tela_personal.mexer_personal() == 2:
#   self.__controlador_sistema.controladoraluno.mexer_aluno()
#     while True:  # aqui ele vai fazer o laço e verificar a opcao do mexer alu.
#         if self.__tela_aluno.mexer_aluno() == 1:  # COntrolador sistema {Dicionario com lista de opcao}
#             self.__controlador_sistema.controladoraluno.incluir_aluno()
#         elif self.__tela_aluno.mexer_aluno() == 2:
#             self.__controlador_sistema.controladoraluno.alterar_aluno()
#         elif self.__tela_aluno.mexer_aluno() == 3:
#             self.__controlador_sistema.controladoraluno.excluir_aluno()
#         elif self.__tela_aluno.mexer_aluno() == 4:
#             self.__controlador_sistema.controladoraluno.listar_alunos()
#         elif self.__tela_aluno.mexer_aluno() == 5:  # Duvida aqui o consultar! COMO fazer? se precisa do cpf
#             self.__controlador_sistema.controladoraluno.consultar_aluno()  # Talvez na tela aluno pedir o cpf
#             # junto e ??
#         elif self.__tela_aluno.mexer_aluno() == 6:
#             self.__controlador_sistema.controladoraluno.retornar()
#         else:
#             self.__tela_personal.mostrar_msg("opcao de escolha invalida")
#             self.tela_alterar_dados_alunos()  # Pode fazer isso? Para voltar ao método


