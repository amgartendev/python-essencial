"""
Doctests

Doctests são testes que colocamos na docstring das funções/métodos Python.

def soma(a, b):
    # Abrir aspas duplas triplas
    soma os números A e B

    >>> soma(1, 2)
    3

    >>> soma(4, 6)
    10
    # Fechar aspas duplas triplas
    return a + b

Para rodar um teste do doctest:
python -m doctest -v nome_do_modulo.py

# Saída

Trying:
    soma(1, 2)
Expecting:
    3
ok
1 items had no tests:
    143-Doctests
1 items passed all tests:
   1 tests in 143-Doctests.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.


# Outro exemplo, aplicando o TDD

def duplicar(valores):
    # Abrir aspas duplas triplas Duplica os valores em uma lista

    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar([])
    []

    >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> duplicar([True, None])
    TraceBack (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    # Fechar aspas duplas triplas
    return [2 * elemento for elemento in valores]

# Erro inesperado...

# OBS: Dentro do doctest, o Python não reconhece string com aspas duplas. Precisa ser aspas simples.

def fala_oi():
    # Expected: "oi"
    # Got: 'oi'

    "Abrir aspas duplas Fala oi
    >>> fala_oi()
    'oi'
    # Fechar aspas duplas
    return "oi"
"""


# Um último caso estranho...

def verdade():
    """Retorna verdade

    >>> verdade()
    True
    """
    return True
