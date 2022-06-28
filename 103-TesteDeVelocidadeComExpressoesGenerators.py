"""
Teste de Velocidade com Expressões Geradoras

# Generators (Geradores)


def num():
    for num in range(1, 10):
        yield num


generator1 = num()

print(generator1)  # Generator

print(next(generator1))
print(next(generator1))


# Generator Expression

generator2 = (num for num in range(1, 10))

print(generator2)  # Generator Expression

print(next(generator2))
print(next(generator2))
"""

# Realizando o teste de velocidade
import time

# Generator Expression

generator_inicio = time.time()
print(sum(num for num in range(100000000)))  # 100 milhões
generator_tempo = time.time() - generator_inicio


# List Comprehension

list_inicio = time.time()
print(sum([num for num in range(100000000)]))  # 100 milhões
list_tempo = time.time() - list_inicio

print(f'Generator Expression: {generator_tempo}')
print(f'List Comprehension: {list_tempo}')
