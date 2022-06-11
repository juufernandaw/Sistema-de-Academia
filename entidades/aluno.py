from entidades.usuario import Usuario


class Aluno(Usuario):

    def __init__(self, nome: str, login: str, senha: str, cpf: str):
        super().__init__(nome, login, senha, cpf)
        self.__treinos = []

    @property
    def treinos(self):
        return self.__treinos
