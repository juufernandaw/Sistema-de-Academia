from controladoraluno import ControladorAluno
from controladortreino import ControladorTreino
from controladortreinodiario import ControladorTreinoDiario
from controladorpersonaltrainer import ControladorPersonalTrainer
from telas.telasistema import TelaSistema

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

    def iniciar_tela(self):
        pass

    def encerrar_sistema(self):
        exit(0)

