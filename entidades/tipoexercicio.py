class TipoExercicio():
    def __init__(self, categoria_exercicio: str, qtd_kcal_gasta: int):
        self.__categoria_exercicio = categoria_exercicio
        self.__qtd_kcal_gasta = qtd_kcal_gasta

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

