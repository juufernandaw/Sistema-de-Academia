
class ValueErrorException(Exception):
    def __init__(self):
        self.mensagem = "Valor digitado incorreto, tente novamente."
        super().__init__(self.mensagem)
