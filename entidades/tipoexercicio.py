class TipoExercicio():
    def __init__(self, categoria_exercicio: str, qtd_kcal_gasta: int):
        self.__categoria_exercicio = categoria_exercicio
        self.__qtd_kcal_gasta = qtd_kcal_gasta
        self.__tipos_exercicio = [TipoExercicio("Muscular - Superior",200), TipoExercicio("Muscular - Inferior",150), \
        TipoExercicio("Cardiovascular",300)]

    @property
    def categoria_exercicio(self):
        return self.__categoria_exercicio

    @categoria_exercicio.setter
    def categoria_exercicio(self, categoria_exercicio: str):
        self.__categoria_exercicio = categoria_exercicio

    @property
    def qtd_kcal_gasta(self):
        return self.__qtd_kcal_gasta

    @qtd_kcal_gasta.setter
    def qtd_kcal_gasta(self, qtd_kcal_gasta: str):
        self.__qtd_kcal_gasta = qtd_kcal_gasta

    @property
    def tipos_exercicio(self):
        return self.__tipos_exercicio