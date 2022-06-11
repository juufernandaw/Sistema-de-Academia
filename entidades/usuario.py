from abc import ABC, abstractmethod


class Usuario(ABC):
    @abstractmethod
    def __init__(self, nome: str, login: str, senha: str, cpf: str):
        pass

    @abstractmethod
    @property
    def nome(self):
        pass

    @abstractmethod
    @nome.setter
    def nome(self, nome: str):
        pass

    @abstractmethod
    @property
    def login(self):
        pass

    @abstractmethod
    @login.setter
    def login(self, login: str):
        pass

    @abstractmethod
    @property
    def senha(self):
        pass

    @abstractmethod
    @senha.setter
    def nome(self, senha: str):
        pass

    @abstractmethod
    @property
    def cpf(self):
        pass

    @abstractmethod
    @cpf.setter
    def cpf(self, cpf: str):
        pass


