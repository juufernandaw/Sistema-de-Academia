from telas.telaaluno import TelaAluno
from entidades.aluno import Aluno


class ControladorAluno():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__alunos = []
        self.__tela_aluno = TelaAluno()

    @property
    def alunos(self):
        return self.__alunos

    def verificar_login_senha(self, login, senha):  # VERIFICAR o login e senha.
        if isinstance(login, str) and isinstance(senha, str):
            try:
                for aluno in self.__alunos:
                    if (aluno.login == login) and (aluno.senha == senha):
                        return True, aluno  # aluno q achou retornar
                    if not aluno.login and not aluno.senha:
                        raise TypeError
            except TypeError:
                self.__tela_aluno.mostrar_msg("Login e senha inválidos")
            else:
                return False

    def vincular_aluno_treino(self, aluno: Aluno, treino):
        aluno.adicionar_treino_aluno(treino)

    def desvincular_aluno_treino(self, aluno: Aluno, treino):
        aluno.remover_treino_aluno(treino)

    def incluir_aluno(self):
        dados_aluno = self.__tela_aluno.pega_dados_aluno()
        for aluno in self.__alunos:
            if dados_aluno["login"] == aluno.login:
                self.__tela_aluno.mostrar_msg("Este login já consta no sistema!")
                return self.incluir_aluno()
            elif dados_aluno["cpf"] == aluno.cpf:
                self.__tela_aluno.mostrar_msg("Este cpf já consta no sistema!")
                return self.incluir_aluno()
        else:
            aluno = Aluno(dados_aluno["nome"], dados_aluno["login"], dados_aluno["senha"], dados_aluno["cpf"])
            self.__alunos.append(aluno)
            if aluno is not None:
                self.__tela_aluno.mostrar_msg("Aluno cadastrado com sucesso!")
                return self.abre_tela_funcoes_aluno()

    def selecionar_aluno(self):
        cpf_aluno = self.__tela_aluno.pegar_cpf()
        for aluno in self.__alunos:
            if aluno.cpf == cpf_aluno:
                return aluno
        else:
            return None

    def buscar_aluno_por_treino(self, treino):
        for aluno in self.__alunos:
            for treino_individual in aluno.treinos:
                if treino_individual.nome == treino.nome:
                    return aluno
        else:
            return None

    def alterar_aluno(self):
        aluno = self.selecionar_aluno()
        aluno_novo = self.__tela_aluno.layout_alterar_aluno(aluno)
        aluno.nome = aluno_novo["nome"]
        aluno.cpf = aluno_novo["cpf"]
        aluno.login = aluno_novo["login"]
        aluno.senha = aluno_novo["senha"]
        print("aluno nome", aluno.nome, "aluno cpf", aluno.cpf, "aluno login", aluno.login, "aluno senha", aluno.senha)
        if aluno_novo is not None:
            self.__tela_aluno.mostrar_msg("Aluno alterado com sucesso!")
        return self.abre_tela_funcoes_aluno()

    def excluir_aluno(self):
        try:
            aluno = self.selecionar_aluno()
            if aluno is not None:
                self.__alunos.remove(aluno)
                self.__tela_aluno.mostrar_msg("Aluno removido com sucesso!")
                return self.abre_tela_funcoes_aluno()
            else:
                raise Exception
        except Exception:
            self.__tela_aluno.mostrar_msg("ATENCAO: aluno não existente. Favor escolher um aluno existente.")
            return self.excluir_aluno()

    def consultar_aluno(self):
        try:
            cpf = self.__tela_aluno.pegar_cpf()
            for aluno in self.__alunos:
                if aluno.cpf == cpf:
                    print("Entrouuu")
                    self.__tela_aluno.mostrar_aluno([ #pra tela mostra em formato de dict
                        {"nome": aluno.nome, "login": aluno.login, "senha": aluno.senha, "cpf": aluno.cpf,
                         "treinos": aluno.treinos}])
                    return self.abre_tela_funcoes_aluno()
            else:
                raise Exception
        except Exception:
            self.__tela_aluno.mostrar_msg("ATENCAO: aluno não existente. Favor escolher um aluno existente.")
            return self.abre_tela_funcoes_aluno()

    def listar_alunos(self):
        dict_alunos = []
        for aluno in self.__alunos:
            dict_alunos.append({"nome": aluno.nome, "login": aluno.login, "senha": aluno.senha, "cpf": aluno.cpf,
                 "treinos": aluno.treinos})
        if self.__alunos == []:
            self.__tela_aluno.mostrar_msg("Não há nenhum aluno cadastrado")
        else:
            self.__tela_aluno.mostrar_aluno(dict_alunos)
        return self.abre_tela_funcoes_aluno()

    def abre_tela_funcoes_aluno(self):
            lista_opcoes = {1: self.incluir_aluno, 2: self.alterar_aluno,
                            3: self.excluir_aluno, 4: self.listar_alunos, 5: self.consultar_aluno,
                            6: self.__controlador_sistema.controlador_treino_diario.achar_desempenho_aluno_personal,
                            0: self.retornar
                            }
            while True:
                opcao = self.__tela_aluno.mexer_aluno()
                funcao_escolhida = lista_opcoes[opcao]
                return funcao_escolhida()

    def retornar(self):
        return self.__controlador_sistema.controlador_personal_trainer.abre_tela_inicial()

    def abre_tela_inicial(self):  # abre a tela aluno pós login da tela
        try:
            usuario = self.__controlador_sistema.usuario_logado
            mexer_aluno_opcoes = {1: self.consultar_treino_aluno,
                                  2: self.__controlador_sistema.controlador_treino_diario.mostrar_tela_treino_diario,
                                  0: self.retornar
                                  }
            while True:
                opcao_escolhida = self.__tela_aluno.abre_tela_inicial_tela_aluno()
                if opcao_escolhida != 1 and opcao_escolhida != 2 and opcao_escolhida != 0:
                    raise ValueError
                if opcao_escolhida == 1:
                    return self.consultar_treino_aluno(usuario.treinos)
                else:
                    funcao_escolhida = mexer_aluno_opcoes[opcao_escolhida]
                    return funcao_escolhida()
        except ValueError:
            self.__tela_aluno.mostrar_msg("Digite uma das opções sugeridas, por favor")
            self.abre_tela_inicial()

    def consultar_treino_aluno(self, treinos): #para o aluno ter acesso ao treino
        self.__controlador_sistema.controlador_treino.tela_treino.mostrar_tela_treino(treinos)
        return self.abre_tela_inicial()
