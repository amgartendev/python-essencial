"""
Preservando Metadatas com Wraps

Metadata -> São dados intrísecos em arquivos.

Wraps -> São funções que envolvem elementos com diversas finalidades.


# Problema


def ver_log(funcao):
    def logar(*args, **kwargs):
        # Eu sou uma função (logar) dentro de outra
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    # Soma dois números
    return a + b


# print(soma(10, 30))

print(soma.__name__)  # Esperamos: soma
print(soma.__doc__)  # Esperamos: Soma dois números
"""


# Resolução

from functools import wraps


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números"""
    return a + b


# print(soma(10, 30))

print(soma.__name__)  # Esperamos: soma
print(soma.__doc__)  # Esperamos: Soma dois números

print(help(soma))
