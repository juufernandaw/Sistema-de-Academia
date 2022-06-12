from TrabalhoPOO.entidades.treinodiario import TreinoDiario
from TrabalhoPOO.telas.telatreinodiario import TelaTreinoDiario


class ControladorTreinoDiario():
    def __init__(self, controlador_sistema):
        self.__treinos_diarios = TreinoDiario()
        self.__tela_treinoDiario = TelaTreinoDiario()
        self.__manter_telas = bool
        self.__controlador_sistemas = controlador_sistema

    def desempenho_aluno(self):
        pass

    def checkin(self):
        pass
