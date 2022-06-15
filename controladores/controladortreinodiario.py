from TrabalhoPOO.entidades.treinodiario import TreinoDiario
from TrabalhoPOO.telas.telatreinodiario import TelaTreinoDiario
from TrabalhoPOO.controladores.controladorsistema import ControladorSistema
from TrabalhoPOO.entidades.treino import Treino
from TrabalhoPOO.controladores.controladoraluno import ControladorAluno


class ControladorTreinoDiario():
    def __init__(self, controlador_sistema):
        self.__treinos_diarios = [] # precisa disso ? acho q n precisa
        self.__treinos = []
        self.__tela_treinoDiario = TelaTreinoDiario()
        self.__manter_tela = bool
        self.__controlador_sistema = controlador_sistema

    # def treino_diarios(self):
    #     return self.__treinos_diarios
    #
    # def adc_treinos_diarios(self, treino_diario: TreinoDiario):
    #     self.__treinos_diarios.append(treino_diario)

    def incluir_treino(self, treino: Treino):
        if isinstance(treino, Treino):
            self.__treinos.append(treino)

    def mostrar_tela_treino_diario(self):
        return self.__tela_treinoDiario.mostrar_tela_desempenho()

    def desempenho_aluno(self):  # perguntar sobre como consultar o desempenho aluno
        if self.__tela_treinoDiario.mostrar_tela_desempenho() == 1:
            self.__tela_treinoDiario.mostrar_desempenho()
            self.__tela_treinoDiario.checkin()
            self.checkin()
            cpf = self.__controlador_sistema.controladoraluno.consultar_aluno()
            lista_alunos = self.__controlador_sistema.controladoraluno.listar_alunos()
            for cpf in lista_alunos:

                pass

    def checkin(self):
        checkin = 0
        if self.__controlador_sistema.controladorsistema.abre_logins() == \
                self.__controlador_sistema.controladoraluno.abre_tela_funcoes_aluno():
            checkin += 1

        return checkin
