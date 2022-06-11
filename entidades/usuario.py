from abc import ABC, abstractmethod


class Usuario(ABC):
    @abstractmethod
    def __init__(self, nome: str, login: str, senha: str, cpf: str):
        pass

    @property
    def nome(self):
        pass

    @nome.setter
    def nome(self, nome: str):
        pass

    @property
    def login(self):
        pass

    @login.setter
    def login(self, login: str):
        pass

    @property
    def senha(self):
        pass

    @senha.setter
    def nome(self, senha: str):
        pass

    @property
    def cpf(self):
        pass

    @cpf.setter
    def cpf(self, cpf: str):
        pass


