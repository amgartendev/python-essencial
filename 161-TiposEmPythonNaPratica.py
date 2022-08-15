"""
Tipos em Python na Prática

# Da mesma forma que usamos Type Hinting com str, int, float e bool, podemos utilizar com as coleções
nomes: list = ['João', 'Thiago']

versoes: tuple = (3, 4, 7)

opcoes: dict = {'ar': True, 'banco_couro': True}

valores: set = {3, 4, 5, 6}

print(nomes)
print(versoes)
print(opcoes)
print(valores)
print(__annotations__)


# Para especificarmos o tipo do dado dentro das coleções, precisamos importar a biblioteca typing
from typing import Dict, List, Tuple, Set

nomes: List[str] = ['João', 'Thiago']

versoes: Tuple[int, int, int] = (3, 4, 7)

# Dict[chave, valor]
opcoes: Dict[str, bool] = {'ar': True, 'banco_couro': True}

valores: Set[int] = {3, 4, 5, 6}

print(nomes)
print(versoes)
print(opcoes)
print(valores)
print(__annotations__)


# Jogo de Cartas V1 - Sem Type Hints

import random

NAIPES = '♠ ♥ ♣ ♦'.split()
CARTAS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


def criar_baralho(aleatorio=False):
    # Cria um baralho com 52 cartas
    baralho = [(naipe, carta) for carta in CARTAS for naipe in NAIPES]
    if aleatorio:
        random.shuffle(baralho)
    return baralho


def distribuir_cartas(baralho):
    # Gerencia a mão de cartas de acordo com o baralho gerado
    return baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4]


def jogar():
    # Inicia um jogo de cartas para 4 jogadores
    cartas = criar_baralho(aleatorio=True)
    jogadores = 'P1 P2 P3 P4'.split()
    maos = {jogador: mao for jogador, mao in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        carta = ' '.join(f"{j}{c}" for (j, c) in cartas)
        print(f'{jogador}: {carta}')


if __name__ == '__main__':
    jogar()
"""

# Jogo de Cartas V2 - Com Type Hints

from typing import List, Tuple, Dict, Set
import random


NAIPES: List[str] = '♠ ♥ ♣ ♦'.split()
CARTAS: List[str] = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

CARTA = Tuple[str, str]
BARALHO = List[CARTA]


def criar_baralho(aleatorio: bool = False) -> BARALHO:
    """Cria um baralho com 52 cartas"""
    baralho = [(naipe, carta) for carta in CARTAS for naipe in NAIPES]
    if aleatorio:
        random.shuffle(baralho)
    return baralho


def distribuir_cartas(baralho: BARALHO) -> Tuple[BARALHO, BARALHO, BARALHO, BARALHO]:
    """Gerencia a mão de cartas de acordo com o baralho gerado"""
    return baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4]


def jogar() -> None:
    """Inicia um jogo de cartas para 4 jogadores"""
    cartas = criar_baralho(aleatorio=True)
    jogadores = 'P1 P2 P3 P4'.split()
    maos = {jogador: mao for jogador, mao in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        carta = ' '.join(f"{j}{c}" for (j, c) in cartas)
        print(f'{jogador}: {carta}')


if __name__ == '__main__':
    jogar()
