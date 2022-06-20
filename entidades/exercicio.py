# from entidades.tipoexercicio import TipoExercicio
from TrabalhoPOO.entidades.tipoexercicio import TipoExercicio


class Exercicio():
    def __init__(self, nome: str, serie: int, repeticao: int, tempo_descanso: int, tipo_exercicio: TipoExercicio):
        self.__nome = nome
        self.__serie = serie
        self.__repeticao = repeticao
        self.__tempo_descanso = tempo_descanso
        self.__tipo_exercicio = tipo_exercicio

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def serie(self):
        return self.__serie

    @serie.setter
    def serie(self, serie: int):
        self.__serie = serie

    @property
    def repeticao(self):
        return self.__repeticao

    @repeticao.setter
    def repeticao(self, repeticao: str):
        self.__repeticao = repeticao

    @property
    def tempo_descanso(self):
        return self.__tempo_descanso

    @tempo_descanso.setter
    def tempo_descanso(self, tempo_descanso: int):
        self.__tempo_descanso = tempo_descanso

    @property
    def tipo_exercicio(self):
        return self.__tipo_exercicio

    @tipo_exercicio.setter
    def tipo_exercicio(self, tipo_exercicio: TipoExercicio):
        self.__tipo_exercicio = tipo_exercicio
