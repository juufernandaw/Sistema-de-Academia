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

    def abre_logins(self):
        lista_opcoes = {1: self.controlador_aluno.abre_tela_inicial,
                        2: self.controlador_personal_trainer.abre_tela_inicial,
                        0: self.encerrar_sistema}
        while True:
            opcao_escolhida = self.__tela_sistema.mostrarMenu_inicial()
            if opcao_escolhida == 1:
                self.__tela_sistema.logar(1) #se for vdd ele vai entrar no menu de cada: aluno ou personal
                verficar = self.__controlador_aluno.verificar_login_senha()
                if verficar:
                    funcao_escolhida = lista_opcoes[opcao_escolhida]
                    funcao_escolhida()
                else:
                    self.logar(f"{opcao_escolhida} invalida, digite 1, 2 ou 0 para sair. ")
                    
            elif opcao_escolhida == 2:
                self.__tela_sistema.logar(2)
                if self.__controlador_aluno.verificar_login_senha(): #perguntar
                    funcao_escolhida = lista_opcoes[opcao_escolhida]
                    funcao_escolhida()
            elif opcao_escolhida == 0:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()

    def iniciar_tela_sistema(self):
        self.__tela_sistema.mostrarMenu_inicial()

    def encerrar_sistema(self):
        exit(0)
