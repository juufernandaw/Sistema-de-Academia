class TipoExercicio():
    def __init__(self, categoria_exercicio: str, qtd_kcal_gasta: int):
        self.__categoria_exercicio = categoria_exercicio
        self.__qtd_kcal_gasta = qtd_kcal_gasta
        self.__tipos_exercicio = [{"categoria_exercicio":"Muscular - Superior", "qtd_kcal_gasta":200}, \
        {"categoria_exercicio":"Muscular - Inferior", "qtd_kcal_gasta":150}, \
        {"categoria_exercicio":"Cardiovascular", "qtd_kcal_gasta":350}] #checar se é assim

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