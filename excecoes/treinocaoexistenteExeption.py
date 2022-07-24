
class TreinoNaoExistenteException(Exception):
    def __init__(self):
        self.mensagem = "ATENÇÃO: Treino não existente. Favor digitar um treino válido."
        super().__init__(self.mensagem)
