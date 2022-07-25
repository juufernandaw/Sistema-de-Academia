from persistencia.DAO import DAO
from entidades.treinodiario import TreinoDiario


class TreinoDiarioDAO(DAO):
    def __init__(self):
        super().__init__("treinodiario.pkl")

    def add(self, treino_diario: TreinoDiario):
        if treino_diario is not None:
            super().add(treino_diario.chave(), treino_diario)  # passa a chave e o objeto

    def get(self, treino_diario: TreinoDiario):
        return super().get(treino_diario.chave())

    def remove(self, treino_diario: TreinoDiario):
        super().remove(treino_diario.chave())
