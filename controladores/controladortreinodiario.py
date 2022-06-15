from TrabalhoPOO.entidades.treinodiario import TreinoDiario
from TrabalhoPOO.telas.telatreinodiario import TelaTreinoDiario
from TrabalhoPOO.controladores.controladorsistema import ControladorSistema

class ControladorTreinoDiario():
    def __init__(self, controlador_sistema):
        self.__treinos_diarios = []
        self.__tela_treinoDiario = TelaTreinoDiario()
        self.__manter_tela = bool
        self.__controlador_sistema = controlador_sistema


    @property
    def treino_diarios(self):
        return self.__treinos_diarios

    def adc_treinos_diarios(self, treino_diario: TreinoDiario):
        self.__treinos_diarios.append(treino_diario)

    def desempenho_aluno(self):
        self.__controlador_sistema.controladoraluno.listar_alunos()
        self.checkin()

    def checkin(self):
        checkin = 0
        if self.__controlador_sistema.controladorsistema.abre_logins() == \
            self.__controlador_sistema.controladoraluno.abre_tela_funcoes_aluno():
            checkin += 1

        return checkin
