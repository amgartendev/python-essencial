"""
Módulo Random e o que são módulos?

- Em Python, módulos nada mais são do que outros arquivos Python.

Módulo Random -> Possui várias funções para geração de números pseudo-aleatório.

# OBS: Existem duas formas de se utilizar um módulo ou função deste

# Forma 1 - Importando o módulo inteiro

import random

# random() -> Gera um número real pseudo-aleatório entre 0 e 1.

# OBS: Ao realizar o import inteiro do módulo todas as funções, atríbutos, classes e propriedades que estiverem
# dentro do módulo ficarão disponíveis (ficarão em memória). Caso você saiba que funções você precisa utilizar
# deste módulo, então esta não seria a forma ideal de utilização. Nós veremos uma forma melhor na forma 2.

print(random.random())

# Veja que para utilizar a função random() do pacote random, nós colocamos o nome do pacote e o nome da função,
# separados por ponto.

# OBS: Não confunda a função random() com o pacote random. Pode parecer confuso, mas a função random() é
# apenas uma função dentro do módulo random.

# Forma 2 - Importando uma função específica do módulo (Forma Recomendada)

from random import random

# No import acima, estamos falando: Do módulo random, importe a função random()

for i in range(10):
    print(random())

# uniform() -> Gera um número real pseudo-aleatório entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(5, 10))  # 10 não é incluído


# randint() -> Gera valores pseudo-aleatórios entre os valores estabelecidos.
from random import randint

# Gerador de apostas para MegaSena
for i in range(6):
    print(randint(1, 61), end=' ')  # Começa em 1 e vai até 60

# choice() -> Mostra um valor aleatório entre um iterável

from random import choice

print(choice('Geek University'))
"""

from random import shuffle

# shuffle() -> Tem a função de embaralhar dados

deck = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']

print(deck)

shuffle(deck)

print(deck)
