from persistencia.DAO import DAO
from entidades.personaltrainer import PersonalTrainer

class PersonalDAO(DAO):
    def __int__(self):
        super().__int__("personal.pkl")

    def add(self, personal: PersonalTrainer):
        if personal is not None:
            super().add(personal.habilitacao, personal)  #passa a chave e o objeto

    def get(self, habilitacao: str):
        return super().get(habilitacao)

    def remove(self, personal: PersonalTrainer):
        super().remove(personal.habilitacao)
