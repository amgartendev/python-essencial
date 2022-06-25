"""
Módulo Collections - Named Tuple

https://docs.python.org/3/library/collections.html#collections.namedtuple

# Recap Tupla
tupla = (1, 2, 3)

print(tupla[1])

# Named Tuple -> São tuplas diferenciadas, onde, especificamos um nome para a mesma e também parâmetros.
"""

# Realizando o import

from collections import namedtuple

# Precisamos definir o nome e parâmetros.

# Forma 1 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')

print(ray)


# Acessando os dados 

# Forma 1

print(ray[0])  # Idade
print(ray[1])  # Raça
print(ray[2])  # Nome


# Forma 2

print(ray.idade)  # Idade
print(ray.raca)  # Raça
print(ray.nome)  # Nome

print(ray.index('Chow-Chow'))

print(ray.count('Chow-Chow'))
