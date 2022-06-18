# from telas.telaaluno import TelaAluno
# from entidades.aluno import Aluno
# from controladores.controladorpersonaltrainer import PersonalTrainer
# from controladores.controladorsistema import ControladorSistema

from TrabalhoPOO.telas.telaaluno import TelaAluno
from TrabalhoPOO.entidades.aluno import Aluno
from TrabalhoPOO.controladores.controladorpersonaltrainer import PersonalTrainer


class ControladorAluno():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__alunos = []
        self.__manter_tela = True
        self.__tela_aluno = TelaAluno()

    def verificar_login_senha(self, login, senha):  # VERIFICAR o login e senha.
        if isinstance(login, str) and isinstance(senha, str):
            for aluno in self.__alunos:
                if (aluno.login == login) and (aluno.senha == senha):
                    return True, aluno  # aluno q achou retornar
            else:
                return False

    def incluir_aluno(self): 
        dados_aluno = self.__tela_aluno.pega_dados_aluno()
        aluno = Aluno(dados_aluno["nome"], dados_aluno["login"], dados_aluno["senha"], dados_aluno["cpf"])
        self.__alunos.append(aluno)
        if (aluno is not None):
            self.__tela_aluno.mostrar_msg("Aluno cadastrado com sucesso!")
            return self.abre_tela_funcoes_aluno()

    def selecionar_aluno(self):
        cpf_aluno = self.__tela_aluno.pegar_cpf()
        for aluno in self.__alunos:
            if aluno.cpf == cpf_aluno:
                return aluno
        else:
            self.__tela_aluno.mostrar_msg("ATENCAO: aluno não existente")

    def buscar_aluno_por_treino(self, treino):
        for aluno in self.__alunos:
            for treino_individual in aluno.treinos:
                if treino_individual.nome == treino.nome:
                    return aluno
        else:
            return None

    def alterar_aluno(self):
        aluno = self.selecionar_aluno() 
        if (aluno is not None):
            lista_opcoes = {1: self.alterar_aluno_nome(aluno), 2: self.alterar_aluno_cpf(aluno), 3: self.alterar_aluno_login(aluno), 4: self.alterar_aluno_senha(aluno)}
            opcao_alteracao = self.__tela_aluno.opcao_alterar()  #retorna a opcao escolhida
            alteracao_aluno = lista_opcoes[opcao_alteracao] #executa a alteração
        else:
            self.__tela_aluno.mostrar_msg("ATENCAO: aluno não existente")

    def alterar_aluno_nome(self, aluno: Aluno):
        aluno.nome = self.__tela_aluno.pegar_nome()

    def alterar_aluno_cpf(self, aluno: Aluno):
        aluno.cpf = self.__tela_aluno.pegar_cpf()

    def alterar_aluno_login(self, aluno: Aluno):
        aluno.login = self.__tela_aluno.pegar_login()

    def alterar_aluno_senha(self, aluno: Aluno):
        aluno.senha = self.__tela_aluno.pegar_senha()

    def excluir_aluno(self):
        aluno = self.selecionar_aluno() 
        if (aluno is not None):
            self.__alunos.remove(aluno)
        else:
            self.__tela_aluno.mostrar_msg("ATENCAO: aluno não existente")

    def consultar_aluno(self, cpf: str):
        for aluno in self.__alunos:
            if aluno.cpf == cpf:
                return aluno
        return None
        #ajustar visualização das listas

    def listar_alunos(self):
        for aluno in self.__alunos:
            self.__tela_aluno.mostrar_aluno({"nome": aluno.nome, "login": aluno.login, "senha": aluno.senha, "cpf": aluno.cpf, "treinos": aluno.treinos})
        #ajustar visualização das listas

    def abre_tela_funcoes_aluno(self):
        print("Entrei")
        lista_opcoes = {1: self.incluir_aluno, 2: self.alterar_aluno,
                        3: self.excluir_aluno, 4: self.listar_alunos, 5: self.consultar_aluno, 6: self.retornar}
        while True:
            opcao = self.__tela_aluno.mexer_aluno()
            funcao_escolhida = lista_opcoes[opcao]
            return funcao_escolhida()

    def retornar(self):
        pass
