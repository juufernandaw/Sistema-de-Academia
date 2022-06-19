from TrabalhoPOO.entidades.treinodiario import TreinoDiario
from TrabalhoPOO.telas.telatreinodiario import TelaTreinoDiario
from TrabalhoPOO.entidades.treino import Treino
# from TrabalhoPOO.controladores.controladorsistema import ControladorSistema
# from TrabalhoPOO.entidades.treino import Treino
# from TrabalhoPOO.controladores.controladoraluno import ControladorAluno
# from TrabalhoPOO.entidades.aluno import Aluno

# from entidades.treinodiario import TreinoDiario
# from telas.telatreinodiario import TelaTreinoDiario
# from entidades.treino import Treino
# from controladores.controladorsistema import ControladorSistema
# from controladores.controladoraluno import ControladorAluno
# from entidades.aluno import Aluno


class ControladorTreinoDiario():
    def __init__(self, controlador_sistema):
        self.__treinos_diarios = []
        self.__tela_treinoDiario = TelaTreinoDiario()
        self.__manter_tela = bool
        self.__controlador_sistema = controlador_sistema

    @property
    def treino_diarios(self):  # lista de treino diario
        return self.__treinos_diarios

    def mostrar_tela_treino_diario(self): #  ABA Treino Diario
        treino_diario_opcoes = {1: self.confirmar_checkin,
                                2: self.voltar_menu_inicial,
                                3: self.colocar_treino_na_lista_treino_diario
                                }
        while True:
            opcao_treino_diario = self.__tela_treinoDiario.mostrar_tela_desempenho()
            funcao_escolhida = treino_diario_opcoes[opcao_treino_diario]
            return funcao_escolhida()

    def voltar_menu_inicial(self):
        aluno = self.__controlador_sistema.usuario_logado
        if aluno:
            return self.__controlador_sistema.controladoraluno.abre_tela_funcoes_aluno()
        else:
            return self.__controlador_sistema.controladorpersonaltrainer.voltar_ao_menu_personal()

    def desempenho_aluno(self):
        aluno = self.__controlador_sistema.usuario_logado
        self.__tela_treinoDiario.mensagem("Essa é seu desempenho: ")
        contador_presenca = self.checkin()
        treino_diario = TreinoDiario(aluno, contador_presenca, aluno.treinos())
        if treino_diario:
            self.__tela_treinoDiario.checkin(contador_presenca)
            return self.mostrar_tela_treino_diario()

    def adicionar_treino_a_treinodiario(self, escolha_treino: Treino):
        # adiciona o treino escolhido na lista de treinoDiario
        if isinstance(escolha_treino, Treino):
            self.__treinos_diarios.append(escolha_treino)
            self.__tela_treinoDiario.mensagem("Treino iniciado")
            return self.mostrar_tela_treino_diario()

    def confirmar_checkin(self):  # TREINO DIARIO É UMA LISTA DE TREINO!
        aluno = self.__controlador_sistema.usuario_logado
        escolha_treino = self.__tela_treinoDiario.montar_treino_diario(aluno.treinos) # retornar o treino q ele escolheu
        self.adicionar_treino_a_treinodiario(aluno.treinos[escolha_treino])  # colocar o valor da lista para o metodo
        treino_diario = TreinoDiario(aluno, contador_presenca, escolha_treino)


    def checkin(self):
        checkin = False
        conta_presenca = 0
        if self.__controlador_sistema.controladorsistema.abre_logins() == \
                self.__controlador_sistema.controladoraluno.abre_tela_funcoes_aluno():
            checkin = True
            if checkin:
                conta_presenca += 1
        return conta_presenca
