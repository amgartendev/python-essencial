"""
Generator Expression

Em aulas anteriores nós estudamos:
    - List Comprehension;
    - Dictionary Comprehension;
    - Set Comprehension.

Não vimos:
    - Tuple Comprehension... porque elas se chamam Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))

# Poderíamos ter feito utilizando Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

# Qual é a utilidade de getsizeof() ? -> Retorna a quantidade de bytes em memória do elemento passado como parãmetro
from sys import getsizeof 

# Mostra quantos bytes a string 'Geek' está ocupando em mémoria. Quanto maior a string, maior o espaço ocupado
print(getsizeof('Geek'))

print(getsizeof('University'))

print(getsizeof(9))

print(getsizeof(91))

print(getsizeof(92345668823))

print(getsizeof(True))

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])
print(f'Lis Comprehension -- {list_comp} bytes')

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})
print(f'Set Comprehension -- {set_comp} bytes')

# Gerando uma lista de números com Set Comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})
print(f'Dic Comprehension -- {dict_comp} bytes')

# Gerando uma lista de números com Generator
gen = getsizeof(x * 10 for x in range(1000))
print(f'\nGenerator Expression -- {gen} bytes')
"""

# Eu posso iterar no Generator Expression? Sim!

gen = (x * 10 for x in range(1000)) 
print(gen)
print(type(gen))

for num in gen:
    print(num)