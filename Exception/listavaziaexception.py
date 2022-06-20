
class ListaVaziaException(Exception):
    def __init__(self, lista: []):
        self.mensagem = "A lista está vazia, volte e preencha a lista!"
        super().__init__(self.mensagem.format(lista))
