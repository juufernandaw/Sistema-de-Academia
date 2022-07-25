from persistencia.DAO import DAO
from entidades.aluno import Aluno

class AlunoDAO(DAO):
    def __init__(self):
        super().__init__('aluno.pkl')

    def add(self, aluno: Aluno):
        super().add(aluno.cpf, aluno)  #passa a chave e o objeto

    def get(self, cpf_aluno: str):
        return super().get(cpf_aluno)

    def remove(self, aluno: Aluno):
        super().remove(aluno.cpf)
