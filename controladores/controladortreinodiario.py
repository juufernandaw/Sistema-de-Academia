from datetime import date
from entidades.treinodiario import TreinoDiario
from telas.telatreinodiario import TelaTreinoDiario
from entidades.treino import Treino
from excecoes.valueErrorException import ValueErrorException
from excecoes.usuarioinexistenteException import UsuarioInexistenteException


class ControladorTreinoDiario:

    def __init__(self, controlador_sistema):
        self.__lista_treinos = []
        self.__lista_treinos_diarios = []
        self.__tela_treinoDiario = TelaTreinoDiario()
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
                                    0: self.__controlador_sistema.iniciar_tela_sistema
                                    }
            while True:
                opcao_treino_diario = self.__tela_treinoDiario.mostrar_tela_desempenho()
                if opcao_treino_diario != 1 and opcao_treino_diario != 2 and opcao_treino_diario != 0:
                    raise ValueErrorException
                funcao_escolhida = treino_diario_opcoes[opcao_treino_diario]
                return funcao_escolhida()
        except ValueErrorException as e:
            self.__tela_treinoDiario.mensagem(e)
            self.mostrar_tela_treino_diario()

    def verificar_calorias(self, usuario):
        soma_calorias = 0
        for treino_diario in self.__lista_treinos_diarios:  # lista de treinos que tem os treinos
            if treino_diario.aluno == usuario:  # lembrar de validar se é do aluno o treinodiario
                for treino in treino_diario.treinos:
                    for exercicio in treino.exercicios:
                        soma_calorias += exercicio.tipo_exercicio.qtd_kcal_gasta
        return soma_calorias

    def verificar_dias_treino(self, usuario):
        dias_de_treino = 0
        for treinodiario in self.__lista_treinos_diarios:
            if treinodiario.aluno == usuario:
                dias_de_treino += 1
        return dias_de_treino

    def achar_desempenho_aluno_personal(self):
        try:
            aluno_escolhido = None
            cpf_aluno = self.__tela_treinoDiario.printar_tela_escolher_aluno()
            for aluno in self.__controlador_sistema.controlador_aluno.alunos:
                if aluno.cpf == cpf_aluno:
                    for treino_diario in self.__lista_treinos_diarios:
                        if treino_diario.aluno == aluno:
                            aluno_escolhido = aluno
                            dias = self.verificar_dias_treino(aluno_escolhido)
                            calorias = self.verificar_calorias(aluno_escolhido)
                            self.__tela_treinoDiario.mostrar_dias_treino_aluno(aluno_escolhido.cpf, dias)
                            self.__tela_treinoDiario.contar_calorias_aluno(aluno_escolhido.cpf, calorias)
                        elif treino_diario.aluno != aluno:
                            raise UsuarioInexistenteException
            return self.__controlador_sistema.controlador_aluno.abre_tela_funcoes_aluno()
        except UsuarioInexistenteException as e:
            self.__tela_treinoDiario.mensagem(e)
            self.achar_desempenho_aluno_personal()

    def desempenho_aluno(self):
        usuario = self.__controlador_sistema.usuario_logado
        dias_treino = self.verificar_dias_treino(usuario)
        calorias = self.verificar_calorias(usuario)
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
            self.__tela_treinoDiario.listar_treino_escolhido(self.__lista_treinos)
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
        # self.__tela_treinoDiario.listar_treino_escolhido(self.__lista_treinos)

    def voltar_login(self):
        self.__controlador_sistema.iniciar_tela_sistema()
