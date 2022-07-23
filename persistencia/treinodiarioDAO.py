from persistencia.DAO import DAO
from entidades.treinodiario import TreinoDiario
from entidades.aluno import Aluno


class TreinoDiariDAO(DAO):
    def __int__(self):
        super().__int__("treino diario.pkl")

    def add(self, treino_diario: TreinoDiario):
        if treino_diario is not None:
            super().add(treino_diario.chave(), treino_diario)  # passa a chave e o objeto

    def get(self, treino_diario: TreinoDiario):
        return super().get(treino_diario.chave())

    def remove(self, treino_diario: TreinoDiario):
        super().remove(treino_diario.chave())
