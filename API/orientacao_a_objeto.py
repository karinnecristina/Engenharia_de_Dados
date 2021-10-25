import datetime
import math


class Pessoa:
    def __init__(self, nome: str, sobrenome: str, data_nascimento: datetime.date):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

    @property
    def idade(self) -> int:
        return math.floor(
            (datetime.date.today() - self.data_nascimento).days / 365.2425
        )  # considerando os anos bissextos
