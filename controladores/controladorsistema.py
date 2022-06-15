from TrabalhoPOO.controladores.controladoraluno import ControladorAluno
from TrabalhoPOO.controladores.controladortreino import ControladorTreino
from TrabalhoPOO.controladores.controladortreinodiario import ControladorTreinoDiario
from TrabalhoPOO.controladores.controladorpersonaltrainer import ControladorPersonalTrainer
from TrabalhoPOO.telas.telasistema import TelaSistema


class ControladorSistema:

    def __init__(self):
        self.__controlador_treino = ControladorTreino(self)
        self.__controlador_treino_diario = ControladorTreinoDiario(self)
        self.__controlador_aluno = ControladorAluno(self)
        self.__controlador_personal_trainer = ControladorPersonalTrainer(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_treino(self):
        return self.__controlador_treino

    @property
    def controlador_treino_diario(self):
        return self.__controlador_treino_diario

    @property
    def controlador_aluno(self):
        return self.__controlador_aluno

    @property
    def controlador_personal_trainer(self):
        return self.__controlador_personal_trainer

    def abre_logins(self):
        lista_opcoes = {1: self.__controlador_aluno.abre_tela_funcoes_aluno,
                        2: self.__controlador_personal_trainer.abre_tela_inicial,
                        0: self.encerrar_sistema}
        login = None
        senha = None
        while True:
            opcao_escolhida = self.__tela_sistema.mostrarMenu_inicial()
            if opcao_escolhida == 1:
                self.__tela_sistema.logar(1)  # se for vdd ele vai entrar no menu de cada: aluno ou personal
                verficar = self.__controlador_aluno.verificar_login_senha()
                if verficar:
                    funcao_escolhida = lista_opcoes[opcao_escolhida]
                    return funcao_escolhida()
                else:
                    self.__tela_sistema.mostrar_msg_telasistema(f"{opcao_escolhida} invalida, "
                                                                f"digite 1, 2 ou 0 para sair. ")
                    self.__tela_sistema.mostrarMenu_inicial()
            elif opcao_escolhida == 2:
                login, senha = self.__tela_sistema.logar(2)
                if self.__controlador_personal_trainer.verificar_login_senha(login, senha):
                    funcao_escolhida = lista_opcoes[opcao_escolhida]
                    return funcao_escolhida()
            elif opcao_escolhida == 0:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                return funcao_escolhida()

    def iniciar_tela_sistema(self):
        self.__tela_sistema.mostrarMenu_inicial()

    def encerrar_sistema(self):
        exit(0)
