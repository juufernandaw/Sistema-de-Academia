from entidades.tipoexercicio import TipoExercicio

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

        
