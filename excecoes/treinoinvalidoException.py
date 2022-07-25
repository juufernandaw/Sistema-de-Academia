
class TreinoInvalidoException(Exception):
    def __init__(self, lista: []):
        self.mensagem = "ATENÇÃO: Treino inválido. Digite um treino válido."
        super().__init__(self.mensagem)
