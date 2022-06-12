from controladoraluno import ControladorAluno
from controladortreino import ControladorTreino
from controladortreinodiario import ControladorTreinoDiario
from controladorpersonaltrainer import ControladorPersonalTrainer
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

    def logar(self):
        escolha = None
        if self.__tela_sistema == 1:
            print("Bem vindo ao login:")
            print("1: Caso você seja aluno:")
            print("2: Caso você seja professor:")
            escolha = input()
        elif self.__tela_sistema == 0:
            self.encerrar_sistema()
        return escolha

    def abre_logins(self):
        lista_opcoes = {1: 'aluno', 2: 'professor'}
        while True:
            opcao_escolhida = self.__tela_sistema.mostrarMenu_inicial()
            funcao_escolhida = lista_opcoes[opcao_escolhida]

    def iniciar_tela_sistema(self):
        return self.__tela_sistema

    def encerrar_sistema(self):
        exit(0)
