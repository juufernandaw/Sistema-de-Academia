from persistencia.DAO import DAO
from entidades.aluno import Aluno

class AlunoDAO(DAO):
    def __int__(self):
        super().__int__("aluno.pkl")

    def add(self, aluno: Aluno):
        if aluno is not None:
            super().add(aluno.cpf, aluno) #passa a chave e o objeto

    def get(self, cpf_aluno: str):
        return super().get(cpf_aluno)
