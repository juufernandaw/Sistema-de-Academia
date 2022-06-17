from TrabalhoPOO.entidades.treinodiario import TreinoDiario
from TrabalhoPOO.telas.telatreinodiario import TelaTreinoDiario
from TrabalhoPOO.controladores.controladorsistema import ControladorSistema
from TrabalhoPOO.entidades.treino import Treino
from TrabalhoPOO.controladores.controladoraluno import ControladorAluno
from TrabalhoPOO.entidades.aluno import Aluno


class ControladorTreinoDiario():
    def __init__(self, controlador_sistema):
        self.__treinos_diarios = []
        self.__tela_treinoDiario = TelaTreinoDiario()
        self.__manter_tela = bool
        self.__controlador_sistema = controlador_sistema

    @property
    def treino_diarios(self):  # lista de treino diario
        return self.__treinos_diarios

    def mostrar_tela_treino_diario(self):
        return self.__tela_treinoDiario.mostrar_tela_desempenho()

    def desempenho_aluno(self):
        if self.__tela_treinoDiario.mostrar_tela_desempenho() == 1:
            self.__tela_treinoDiario.mostrar_desempenho()
            aluno = self.__controlador_sistema.usuario_logado  # aqui sabe qual aluno foi logado
            treino_aluno = aluno.treinos()  # perguntar ao usuario qual desses voce quer fazer.
                                            # retornar o treino q ele escolheu
            contador_presenca = self.checkin()
            treino_diario = TreinoDiario(aluno, contador_presenca, treino_aluno)
            self.colocar_treino_diario_lista(treino_diario)
            self.__tela_treinoDiario.checkin()
            self.checkin()

    def colocar_treino_diario_lista(self, treino_diario: TreinoDiario):
        treino_diario_aluno = treino_diario
        if isinstance(treino_diario_aluno, TreinoDiario):
            for treinoDiario in self.__treinos_diarios:
                self.__treinos_diarios.append(treino_diario_aluno)


    def checkin(self): #  no aluno tem um método para perguntar se quer checkin la vai chamar pra ca
        # refazer método
        checkin = False  # metodo errado refazer esse aluno
        conta_presenca = 0
        if self.__controlador_sistema.controladorsistema.abre_logins() == \
                self.__controlador_sistema.controladoraluno.abre_tela_funcoes_aluno():
            checkin = True
            if checkin:
                conta_presenca += 1
        return conta_presenca
