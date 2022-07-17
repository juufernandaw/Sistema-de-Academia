from entidades.personaltrainer import PersonalTrainer
from telas.telapersonaltrainer import TelaPersonalTrainer
from telas.telasistema import TelaSistema
from telas.telaaluno import TelaAluno


class ControladorPersonalTrainer():

    def __init__(self, controlador_sistema):
        self.__tela_personal = TelaPersonalTrainer()
        self.__tela_aluno = TelaAluno()
        self.__tela_sistema = TelaSistema()
        self.__controlador_sistema = controlador_sistema
        self.__personal = PersonalTrainer("12345678905", "Judi", "a", "a", "01")  # criou o personal

    @property
    def consultar_personal(self):
        return self.__personal

    def verificar_login_senha(self, login, senha):  # VERIFICAR o login e senha.
        if isinstance(login, str) and isinstance(senha, str):
            if self.__personal.login == login and self.__personal.senha == senha:  # get
                return True

    def abre_tela_inicial(self):  # abre a tela personal pos login da tela do sistema AS ABAS
        try:
            mexer_personal_opcoes = {1: self.abre_tela_funcoes_personal,
                                     2: self.__controlador_sistema.controlador_aluno.abre_tela_funcoes_aluno,
                                     3: self.__controlador_sistema.controlador_treino.abre_tela_funcoes_treino,
                                     0: self.voltar
                                     }
            while True:
                opcao_escolhida = self.__tela_personal.mexer_personal()
                if opcao_escolhida != 1 and opcao_escolhida != 2 and opcao_escolhida != 3 and opcao_escolhida != 0:
                    raise ValueError
                funcao_escolhida = mexer_personal_opcoes[opcao_escolhida]
                return funcao_escolhida()
        except ValueError as e:
            self.__tela_sistema.mostrar_msg(e)
            self.__tela_sistema.mostrar_msg("Valor digitado incorreto, tente novamente.")
            self.abre_tela_inicial()

    def voltar(self):
        return self.abre_tela_inicial()

    def abre_tela_funcoes_personal(self):
        try:
            mexer_personal_opcoes = {1: self.consultar_personal,
                                     2: self.alterar_personal,
                                     0: self.voltar
                                     }
            while True:
                opcao_escolhida = self.__tela_personal.tela_aba_personal()
                if opcao_escolhida != 1 and opcao_escolhida != 2 and opcao_escolhida != 0:
                    raise ValueError
                if opcao_escolhida == 1:
                    self.__tela_personal.mostrar_personal_trainer({"nome": self.__personal.nome,
                                                                   "cpf": self.__personal.cpf,
                                                                   "login": self.__personal.login,
                                                                   "senha": self.__personal.senha,
                                                                   "habilitacao": self.__personal.habilitacao})
                    return self.voltar()
                else:
                    funcao_escolhida = mexer_personal_opcoes[opcao_escolhida]
                    return funcao_escolhida()
        except ValueError as e:
            self.__tela_sistema.mostrar_msg(e)
            self.__tela_sistema.mostrar_msg("Digite novamente, com as opções corretas na tela")
            self.abre_tela_funcoes_personal()

    def alterar_personal(self):  # aqui ele está alterando os dados do personal baseado no dicionario da tela
        if self.__personal is not None:  # OK
            novos_dados = self.__tela_personal.tela_alterar_dados()  # vai ser um dicionario
            self.__personal.nome = novos_dados["nome"]
            self.__personal.cpf = novos_dados["habilitacao"]
            self.__personal.login = novos_dados["login"]
            self.__personal.senha = novos_dados["senha"]
            self.__personal.habilitacao = novos_dados["habilitacao"]

        return self.abre_tela_funcoes_personal()

    def colocar_treino_na_lista_treino_diario(self):
        self.__controlador_sistema.controlador_treino_diario.colocar_treino_na_lista_treino_diario()

    def consultar_tela_desempenho(self):
        return self.__controlador_sistema.controlador_treino_diario.mostrar_tela_treino_diario()

    def sair(self):
        return exit(0)
