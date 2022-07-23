from controladores.controladoraluno import ControladorAluno
from controladores.controladortreino import ControladorTreino
from controladores.controladortreinodiario import ControladorTreinoDiario
from controladores.controladorpersonaltrainer import ControladorPersonalTrainer
from telas.telasistema import TelaSistema


class ControladorSistema:

    def __init__(self):
        self.__controlador_treino = ControladorTreino(self)
        self.__controlador_treino_diario = ControladorTreinoDiario(self)
        self.__controlador_aluno = ControladorAluno(self)
        self.__controlador_personal_trainer = ControladorPersonalTrainer(self)
        self.__tela_sistema = TelaSistema()
        self.__usuario_logado = None

    @property
    def usuario_logado(self):  # conseguimos saber quem logou
        return self.__usuario_logado

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

    def iniciar_tela_sistema(self):  # OK
        global opcao_escolhida
        try:
            login_com_sucesso = None
            lista_opcoes = {1: self.__controlador_aluno.abre_tela_inicial,
                            2: self.__controlador_personal_trainer.abre_tela_inicial,
                            0: self.encerrar_sistema}
            login = None
            senha = None
            while True:
                opcao_escolhida = self.__tela_sistema.mostrar_menu_inicial()
                if opcao_escolhida != 1 and opcao_escolhida != 2 and opcao_escolhida != 0:
                    raise ValueError
                elif opcao_escolhida == 0:
                    self.encerrar_sistema()
                else:
                    login, senha = self.__tela_sistema.logar(opcao_escolhida)  # ele vai entrar no login: aluno ou personal
                if opcao_escolhida == 1:
                    login_com_sucesso, self._usuario_logado = self._controlador_aluno.verificar_login_senha(login,
                                                                                                              senha)
                    if self.__usuario_logado is None:
                        raise TypeError
                elif opcao_escolhida == 2:
                    login_com_sucesso = self.__controlador_personal_trainer.verificar_login_senha(login, senha)
                    if not login_com_sucesso:
                        raise TypeError
                if login_com_sucesso is not None:
                    funcao_escolhida = lista_opcoes[opcao_escolhida]
                    return funcao_escolhida()
        except ValueError as e:
            self.__tela_sistema.mostrar_msg(e)
            self.__tela_sistema.mostrar_msg(f"Erro! Valor incorreto: o Número {opcao_escolhida} é invalido"
                                            f" digite 1, 2 ou 0. ")
            self.iniciar_tela_sistema()
        except TypeError:
            self.__tela_sistema.mostrar_msg("Usuário inexistente. Favor digitar login e senha corretos!")
            self.iniciar_tela_sistema()

    def encerrar_sistema(self):  # OK
        exit(0)
