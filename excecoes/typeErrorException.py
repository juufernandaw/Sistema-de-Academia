
class TypeErrorException(Exception):
    def __init__(self):
        self.mensagem = f"Tente novamente."
        super().__init__(self.mensagem)
