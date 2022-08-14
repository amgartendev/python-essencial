"""
Annotations

Annotations nos ajuda a utilizar o Type Hints.

# Correto
texto: str

# Incorreto
texto:str
text : str


# Correto
function() -> str

# Incorreto
function()->str
function() ->str


# Correto
alinhamento: bool = True

# Incorreto
alinhamento:bool=True
alinhamento : bool = True
alinhamento : bool=True
alinhamento: bool= True


import math


def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio


# Podemos imprimir a annotations da nossa função com __annotations__
# print(circunferencia.__annotations__)

nome: str = 'Geek University'

peso: float = 67.9

# Estamos declarando
ativo: bool

# Estamos inicializando
ativo = True

print(nome)
print(peso)
print(ativo)

print(__annotations__)

"""

# Como seria na Programação Orientada a Objetos


class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome: str = nome
        self.__idade: int = idade
        self.__peso: float = peso

    def andar(self) -> str:
        return f'{self.__nome} está andando...'


pessoa = Pessoa(nome='João', idade=18, peso=75.5)

print(pessoa.__dict__)

# print(pessoa.__annotations__)  # Erro. O objeto Pessoa não possui Annotations

print(pessoa.andar.__annotations__)

print(pessoa.__init__.__annotations__)
