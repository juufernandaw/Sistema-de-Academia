
class ValueErrorException(Exception):
    def __init__(self, valor):
        self.mensagem = f" {valor}: Valor digitado incorreto, tente novamente."
        super().__init__(self.mensagem)
