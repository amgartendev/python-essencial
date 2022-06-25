# ÁREA DE TESTE DE CÓDIGOS

from functools import reduce
from sys import getsizeof


names = ['Joao', 'Viviane', 'Clayton', 'Thiago', 'Weslei', 'Ana', 'Bruna', 'Fernanda']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mult_reduce = lambda x, y: x + y


# ------- Map -------
mult = lambda number: number * 2
print(list(map(mult, numbers)))  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# ------- Filter -------
print(list(filter(lambda number: (number > 5) and (number % 2 == 0), numbers)))  # [6, 8, 10]


# ------- Map + Filter -------
print(list(map(lambda name: f'Sua instrutura se chama {name}', filter(lambda name: len(name) < 4, names))))  # ['Sua instrutora se chama Ana']


# ------- Reduce -------
print(reduce(mult_reduce, numbers))  # 55


# ------- Any -------
print(any([name[0] == 'J' for name in names]))  # True


# ------- All -------
print(all([name[0] == 'J' for name in names]))  # False


# ------- Generator Expression -------
print(f'Lis Comprehension: {getsizeof([x * 10 for x in range(1000)])} bytes')
print(f'Set Comprehension: {getsizeof({x * 10 for x in range(1000)})} bytes')
print(f'Dic Comprehension: {getsizeof({x: x * 10 for x in range(1000)})} bytes')
print(f'Gen: {getsizeof((x * 10 for x in range(1000)))} bytes')


# ------- Sorted -------
string = 'Ola, eu me chamo Joao'
number = 12345
number_reverse = 54321
lista = [1, 2, 3, 4, 5]
lista_reverse = [5, 4, 3, 2, 1]

print(sorted(string))  # [' ', ' ', ' ', ' ', ',', 'J', 'O', 'a', 'a', 'a', 'c', 'e', 'e', 'h', 'l', 'm', 'm', 'o', 'o', 'o', 'u']
print(sorted(string, reverse=True))  # ['u', 'o', 'o', 'o', 'm', 'm', 'l', 'h', 'e', 'e', 'c', 'a', 'a', 'a', 'O', 'J', ',', ' ', ' ', ' ', ' ']
# print(sorted(number))  # Erro -> TypeError: 'int' object is not iterable
# print(sorted(number_reverse))  # Erro -> TypeError: 'int' object is not iterable
print(sorted(lista))  # [1, 2, 3, 4, 5]
print(sorted(lista, reverse=True))  # [5, 4, 3, 2, 1]
print(sorted(lista_reverse))  # [1, 2, 3, 4, 5]
print(sorted(lista_reverse, reverse=True))  # [5, 4, 3, 2, 1]


# ------- Min -------
print(min(1, 5))  # 1
print(min(5, 1))  # 1
print(min(10, 4, 7, 51, 0, 1, 5))  # 0

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll, too young to die", "tocou": 32}
]

print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])  # Dead Skin Mask


# ------- Max -------
print(max(1, 5))  # 5
print(max(5, 1))  # 5
print(max(10, 4, 7, 51, 0, 1, 5))  # 51

print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])  # Too old to rock'in'roll, too young to die


# ------- Reversed -------
lista = [1, 2, 3, 4, 5]
string = 'Olá, eu me chamo João'

print(list(reversed(lista)))
print(list(reversed(string)))

for i in reversed(range(10)):
    print(i)


# ------- Len -------
lista = [1, 2, 3, 4, 5]
tupla = 1, 2, 3, 4, 5
conjunto = {1, 2, 3, 4, 5}
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
string = 'Olá, eu me chamo João'

print(len(lista))
print(len(tupla))
print(len(conjunto))
print(len(dicionario))
print(len(string))


# ------- Abs -------
print(abs(-3.14))
print(abs(-510))
print(abs(3.14))
print(abs(510))


# ------- Sum -------
lista = [1, 2, 3, 4, 5]
tupla = 1, 2, 3, 4, 5
conjunto = {1, 2, 3, 4, 5}
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print(sum(lista))
print(sum(tupla))
print(sum(conjunto))
print(sum(dicionario.values()))

print(sum(lista, 5))
print(sum(tupla, 10))
print(sum(conjunto, 20))
print(sum(dicionario.values(), 1))
print(sum(lista, -10))


# ------- Round -------
print(round(1.1))
print(round(1.2))
print(round(1.3))
print(round(1.4))
print(round(1.5))
print(round(1.6))
print(round(1.7))

print(round(1.12345, 1))
print(round(1.12345, 2))
print(round(1.12345, 3))
print(round(1.12345, 4))
print(round(1.12345, 5))

