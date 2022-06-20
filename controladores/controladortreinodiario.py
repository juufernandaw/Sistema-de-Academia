from datetime import date
from TrabalhoPOO.entidades.treino import Treino
from TrabalhoPOO.entidades.treinodiario import TreinoDiario
from TrabalhoPOO.telas.telatreinodiario import TelaTreinoDiario
# from entidades.treinodiario import TreinoDiario
# from telas.telatreinodiario import TelaTreinoDiario
# from entidades.treino import Treino


class ControladorTreinoDiario():
    def __init__(self, controlador_sistema):
        self.__lista_treinos = []
        self.__lista_treinos_diarios = []
        self.__tela_treinoDiario = TelaTreinoDiario()
        self.__manter_tela = bool
        self.__controlador_sistema = controlador_sistema

    @property
    def treino_diarios(self):  # lista de treino
        return self.__lista_treinos

    @property
    def lista_treinos_diarios(self):  # lista de treino diario
        return self.__lista_treinos_diarios

    def mostrar_tela_treino_diario(self):  # ABA Treino Diario
        try:
            treino_diario_opcoes = {1: self.confirmar_checkin,
                                    2: self.desempenho_aluno,
                                    3: self.__controlador_sistema.controlador_aluno.abre_tela_inicial
                                    }
            while True:
                opcao_treino_diario = self.__tela_treinoDiario.mostrar_tela_desempenho()
                if opcao_treino_diario != 1 and opcao_treino_diario != 2 and opcao_treino_diario != 3:
                    raise ValueError
                funcao_escolhida = treino_diario_opcoes[opcao_treino_diario]
                return funcao_escolhida()
        except ValueError:
            print("Valor digitado incorreto, tente novamente.")
            self.mostrar_tela_treino_diario()

    def voltar_menu_inicial(self):
        return self.__controlador_sistema.controladoraluno.abre_tela_inicial()

    def contabilizar_calorias(self):
        usuario = self.__controlador_sistema.usuario_logado
        soma_calorias = 0
        # lembrar de validar se é do aluno o treinodiario
        for treino_diario in self.__lista_treinos_diarios:  # lista de treinos que tem os treinos
            if treino_diario.aluno == usuario:
                for treino in treino_diario.treinos:
                    for exercicio in treino.exercicios:
                        soma_calorias += exercicio.tipo_exercicio.qtd_kcal_gasta
        return soma_calorias

    def desempenho_aluno(self):
        dias_treino = self.contabilizar_dias_treino()
        calorias = self.contabilizar_calorias()
        self.__tela_treinoDiario.mostrar_dias_treino(dias_treino)
        self.__tela_treinoDiario.contar_calorias(calorias)
        return self.mostrar_tela_treino_diario()

    def adicionar_treino_a_treinos(self, escolha_treino: Treino):
        # adiciona o treino escolhido na lista de treinos
        if isinstance(escolha_treino, Treino):
            self.__lista_treinos.append(escolha_treino)
            self.__tela_treinoDiario.mensagem("Treino iniciado")

    def adicionar_treino_diario_a_treinodiarios(self, treino_diario: TreinoDiario):
        # adiciona o treino diario escolhido na lista de treinoDiario
        if isinstance(treino_diario, TreinoDiario):
            self.__lista_treinos_diarios.append(treino_diario)
            self.__tela_treinoDiario.mensagem("checkin finalizado, bom treino")
            self.__lista_treinos = []  # para que seja renovado a lista de treino para cada aluno
            return self.mostrar_tela_treino_diario()

    def confirmar_checkin(self):  # TREINO DIARIO É UMA LISTA DE TREINO!
        aluno = self.__controlador_sistema.usuario_logado
        dia_atual = date.today()
        escolha_treino = self.__tela_treinoDiario.montar_treino_diario(aluno.treinos)  # retorna treino q ele escolheu
        self.adicionar_treino_a_treinos(aluno.treinos[escolha_treino])  # colocar o valor da lista para o metodo
        opcao = self.__tela_treinoDiario.montar_treino_diario_2()
        while opcao != 2:
            escolha_treino = self.__tela_treinoDiario.montar_treino_diario(aluno.treinos)
            self.adicionar_treino_a_treinos(aluno.treinos[escolha_treino])
            opcao = self.__tela_treinoDiario.montar_treino_diario_2()
        treino_diario = TreinoDiario(aluno, dia_atual, self.__lista_treinos)
        self.adicionar_treino_diario_a_treinodiarios(treino_diario)

    def contabilizar_dias_treino(self):
        dias_de_treino = 0
        for treinodiario in self.__lista_treinos_diarios:
            dias_de_treino += 1
        return dias_de_treino
