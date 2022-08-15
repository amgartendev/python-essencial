"""
Tipos em Comentários

Podemos usar Type Hinting em comentários da seguinte maneira:

import math


def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio


print(circunferencia(8))

# print(circunferencia('joao'))  # Erro

# !!ATENÇÃO!!

# Não devemos criar uma função com Annotations nos comentários e na própria função
# Forma errado
def circunferencia(raio: float) -> float:
    # type: (float) -> float
    return 2 * math.pi * raio

# Em caso de múltiplos argumentos


def cabecalho1(texto, alinhamento=True):
    # type: (str, bool) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'


# Um exemplo de função com Type Hinting nada comum


def cabecalho2(
        texto,  # type: str
        alinhamento=True  # type: bool
):  # type: (...) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'


# Também podemos criar variáveis com tipos em comentários

nome = 'João'  # type: str
"""
