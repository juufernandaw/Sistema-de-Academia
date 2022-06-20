class ValorVazio(Exception):
    def __init__(self, msg):
        self.msg = "Valor vazio. Favor, digite um valor."
        super().__init__(self.msg)