"""
Alocação de Gerenciamento de Memória em Python

# De forma geral

x = 10   # x = 10
y = x  # y = 10

x = x + 1  # x = 11

z = 10  # z = y = 10 -- Python usará o mesmo endereço de memória para variáveis com o mesmo valor

if id(y) == id(z):
    print('y e z apontam para a mesma memória')
else:
    print('y e z apontam para objetos diferentes')


# De forma mais complexa


def funcao2(x):
    x = x + 1
    return x


def funcao1(x):
    x = x * 2
    y = funcao2(x)
    return y


# Principal
y = 5
z = funcao1(y)


#                         RAM
# |------------------------------------------------------|
# |  Memória Stack  |          Memória Heap              |
# |                 |                                    |
# |                 | funcao2    x = 11  funcao1 y = 11  |
# |                 | funcao1    x = 10                  |
# | funcao2()  x    | principal  y = 5                   |
# | funcao1()  y, x |                                    |
# | Principal  y, x |                                    |
# |------------------------------------------------------|
# |       Sistema Operacional, aplicativos               |
# |       e memória compartilhada.                       |
# |------------------------------------------------------|

# Quando a nossa função chega em um return, o frame da função é deletada da memória stack


#                         RAM
# |------------------------------------------------------|
# |  Memória Stack  |          Memória Heap              |
# |                 |                                    |
# |                 | principal z = 11                   |
# |                 |               10                   |
# |                 | principal  y = 5                   |
# |                 |                                    |
# | Principal  y, x |                                    |
# |------------------------------------------------------|
# |       Sistema Operacional, aplicativos               |
# |       e memória compartilhada.                       |
# |------------------------------------------------------|

# -----------------------------------------------------------------------

# Para objetos e referênciações de objetos, o Python trabalha com um contador

#      Objeto Carro 1
# |-----------------------|
# | c1, c2 ----> Carro    |
# |                       |
# |                       |
# |                       |
# |-----------------------|

# |----------------------------------------------|
# |  Objeto           |   Número de Referências  |
# |----------------------------------------------|
# |  Objeto Carro 1   |           2              |
# |----------------------------------------------|

# Quando nós paramos de referenciar um objeto, o mesmo passa a ser um "Dead Object"

#      Objeto Carro 1
# |-----------------------|
# |                       |
# |                       |
# |                       |
# |                       |
# |-----------------------|

# |----------------------------------------------|
# |  Objeto           |   Número de Referências  |
# |----------------------------------------------|
# |  Objeto Carro 1   |      0     Dead Object   |
# |----------------------------------------------|

# Nesse momento, entra em ação o Garbage Collector do Python, procurando todos os Dead Objects
# e anula o objeto, liberando assim espaço na memória. O algoritmo utilizado pelo Garbage Collector
# do Python é chamado de "Reference Counting".

# OBS: Diferentes linguagens de programação utilizam diferentes algoritmos para o Garbage Collector.
# Até mesmo diferentes implementações da linguagem Python utilizam diferentes implementações para o
# Garbage Collector: CPython, PyPy, IronPython, Stackless, Jython...

# Relembrando tudo
    - Métodos e variáveis são criadas na memória stack;
    - Os objetos e instâncias são criadas na memória heap;
    - Um novo stack é criado durante a invocação de uma função ou método;
    - Stacks são destruidas sempre que uma função ou método retorna um valor;
    - Garbage Collector é um mecanismo para limpar Dead Objects.
"""
