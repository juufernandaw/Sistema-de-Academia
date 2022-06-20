

class TreinoJaExistente(Exception):
    def __init__(self, msg):
        self.msg = "Nome de treino já cadastrado para outro treino. Favor, digite outro nome."
        super().__init__(self.msg)

