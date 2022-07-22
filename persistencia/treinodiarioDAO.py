from persistencia.DAO import DAO
from entidades.treinodiario import TreinoDiario
from entidades.aluno import Aluno


class TreinoDiario(DAO):
    def __int__(self):
        super().__int__("treino diario.pkl")

    def add(self, treino_diario: TreinoDiario):
        if treino_diario is not None:
            super().add(treino_diario.aluno)  #passa a chave e o objeto

    def get(self, aluno: Aluno):
        return super().get(aluno)

    def remove(self, treino_diario: TreinoDiario):
        super().remove(treino_diario.aluno)
