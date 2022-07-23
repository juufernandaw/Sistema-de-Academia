
class TypeErrorException(Exception):
    def __init__(self):
        self.mensagem = f"Usuário inexistente, tente novamente."
        super().__init__(self.mensagem)
