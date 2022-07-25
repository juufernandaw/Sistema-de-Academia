from persistencia.DAO import DAO
from entidades.treino import Treino

class TreinoDAO(DAO):
    def __init__(self):
        super().__init__('treino.pkl')

    def add(self, treino: Treino):
        super().add(treino.nome, treino)  #passa a chave e o objeto

    def get(self, nome_treino: str):
        return super().get(nome_treino)

    def remove(self, treino: Treino):
        super().remove(treino.nome)
