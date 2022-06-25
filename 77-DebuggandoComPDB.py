"""
Debuggando com PDB

PDB -> Python Debugger

Vida de Inseto -> Life's Bug

Bug -> Inseto

# OBS: A utilização do print() para debugar código é uma prática ruim


def dividir(x, y):
    print(f'X = {x} .. Y = {y}')
    try:
        return int(x) / int(y)
    except (ValueError, ZeroDivisionError) as error:
        return f'Ocorreu um erro: {error}'


print(dividir(4, 7))

# Existem formas mais profissionais de se fazer esse debug. Utilizando o debugger
# Em Python podemos fazer isso em diferentes IDEs, como o PyCharm e IntelliJ ou o utilizando
# o PDB - Python Debugger

# Exemplo com o IntelliJ


def dividir(x, y):
    try:
        return int(x) / int(y)
    except (ValueError, ZeroDivisionError) as error:
        return f'Ocorreu um erro: {error}'


print(dividir(4, 0))

# Exemplo com o PDB - Python Debugger - Exemplo 1

# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e então utilizar a função set_trace()

# Comandos básicos do PDB
# l - Listar onde estamos no código
# n - Próxima linha
# p - Imprime variável
# c - Continua a execução - Finaliza o debugging

import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Exemplo com o PDB - Python Debugger - Exemplo 2

# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e então utilizar a função set_trace()

# Comandos básicos do PDB
# l - Listar onde estamos no código
# n - Próxima linha
# p - Imprime variável
# c - Continua a execução - Finaliza o debugging

nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Por que utilizar este formato?
# O Debug é utilizado durante o desenvolvimento. Costumamos realizar todos os imports de bibliotecas
# no início do arquivo. Por isso, ao invés de  colocarmos o import do pdb no início do arquivo,
# nós colocamos somente onde vamos debuggar, e ao finalizar já fazemos a remoção.

# Exemplo com o PDB - Python Debugger - Exemplo 3

# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e então utilizar a função set_trace()

# * A partir Python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando de debug foi
# incorporado como função built-in (integrada) chamada breakpoint()

# Comandos básicos do PDB
# l - Listar onde estamos no código
# n - Próxima linha
# p - Imprime variável
# c - Continua a execução - Finaliza o debugging

nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Por que utilizar este formato?
# O Debug é utilizado durante o desenvolvimento. Costumamos realizar todos os imports de bibliotecas
# no início do arquivo. Por isso, ao invés de  colocarmos o import do pdb no início do arquivo,
# nós colocamos somente onde vamos debuggar, e ao finalizar já fazemos a remoção.

# OBS: Cuidado com conflitos entre nomes de variáveis e os comandos do PDB


def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c


print(soma(1, 3, 5, 7))

# Como os nomes da variáveis são os mesmos dos comandos do PDB, devemos utilizar o comando p para imprimir
# as variáveis. Ou seja: p nome_da_variavel


# Nada de colocar nomes não representativos em variáveis. Sempre optar por nomes significativos


def soma(num1, num2, num3, num4):
    breakpoint()
    return num1 + num2 + num3 + num4
"""
