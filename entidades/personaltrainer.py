from TrabalhoPOO.entidades.usuario import Usuario


# from entidades.usuario import Usuario


class PersonalTrainer(Usuario):
    def __init__(self, cpf: str, nome: str, login: str, senha: str, habilitacao: str):
        super().__init__(nome, login, senha, cpf)
        self.__habilitacao = habilitacao

    @property
    def habilitacao(self):
        return self.__habilitacao

    @habilitacao.setter
    def habilitacao(self, habilitacao):
        self.__habilitacao = habilitacao
