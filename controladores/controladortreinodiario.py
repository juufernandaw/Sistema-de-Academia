from TrabalhoPOO.entidades.treinodiario import TreinoDiario
from TrabalhoPOO.telas.telatreinodiario import TelaTreinoDiario
from TrabalhoPOO.entidades.treino import Treino


# from TrabalhoPOO.controladores.controladorsistema import ControladorSistema
# from TrabalhoPOO.entidades.treino import Treino
# from TrabalhoPOO.controladores.controladoraluno import ControladorAluno
# from TrabalhoPOO.entidades.aluno import Aluno


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
        treino_diario_opcoes = {1: self.desempenho_aluno,
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

    def colocar_treino_na_lista_treino_diario(self):
        aluno = self.__controlador_sistema.usuario_logado
        treino_aluno = aluno.treinos()
        for treino in self.__treinos_diarios:
            self.__treinos_diarios.append(treino_aluno)
        return self.mostrar_tela_treino_diario()

    def escolher_treino_aluno(self):  # TREINO DIARIO É UMA LISTA DE TREINO!
        self.__tela_treinoDiario.mensagem("Qual treino você quer ? ")
        aluno = self.__controlador_sistema.usuario_logado  # aqui sabe qual aluno foi logado
        treino_aluno = aluno.treinos()  # perguntar ao usuario qual desses voce quer fazer.
        contador_presenca = self.checkin()  # retornar o treino q ele escolheu
        treino_diario_aluno = TreinoDiario(aluno, contador_presenca, aluno.treinos())
        self.__tela_treinoDiario.mensagem("Escolha o seu treino de hoje: ")
        for treino in self.__treinos_diarios:
            print(treino)

    def escolher_treino(self):
        pass

    def checkin(self):  # no aluno tem um método para perguntar se quer checkin la vai chamar pra ca
        # refazer método
        checkin = False  # metodo errado refazer esse aluno
        conta_presenca = 0
        if self.__controlador_sistema.controladorsistema.abre_logins() == \
                self.__controlador_sistema.controladoraluno.abre_tela_funcoes_aluno():
            checkin = True
            if checkin:
                conta_presenca += 1
        return conta_presenca

    # #def método(self): -> em controlador_teladiario
    # aluno = self.__controlador_sistema.usuario_logado
    # escolha_treino = self.__tela_treinoDiario.montar_treino_diario(aluno.treinos)
    # self.adicionar_treino_a_treinodiario(escolha_treino)
    #
    # #def montar_treino_diario: ->em tela_Diario
    #     for treino in lista_treinos:
    #         print("Nome do treino:", treino.nome)
    #     resposta = input("Qual treino você fará hoje?")
    #     return resposta


    
