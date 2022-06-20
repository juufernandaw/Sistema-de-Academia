
class TypeErrorException(Exception):
    def __init__(self, valor):
        self.mensagem = f"Inexistente, tente novamente."
        super().__init__(self.mensagem)
