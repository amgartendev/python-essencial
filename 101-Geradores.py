"""
Geradores

- Geradores (Generators) são Iterators (Iteradores)

OBS: O contrário não é verdadeiro. Ou seja, nem todo iterator é um generator.

Outras informações:
- Generators podem ser criados com funções geradoras;
- Funções geradores utilizam a palvra reservada yield;
- Generators podem ser criados com Expressões Geradoras.

Diferenças entre Funções e Generators Functions (Funções Geradoras)

----------------------------------------------------------------------------------------------
| Funções                                           | Generator Functions                    |
----------------------------------------------------------------------------------------------
| Utilizam return                                   | Utilizam yield                         |
----------------------------------------------------------------------------------------------
| Retorna uma vez                                   | Pode utilizar yield múltiplas vezes    |
----------------------------------------------------------------------------------------------
| Quando executada, retorna um valor                | Quando executada, retorna um generator |
----------------------------------------------------------------------------------------------


# OBS: Uma Generator Function não é um Generator. Ela gera um generator

gen = conta_ate(5)

# print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print(next(gen))  # 1

print('Geek')

for num in gen:
    print(num)
"""

# Exemplo Função Geradora (Generator Function)


def conta_ate(valor_max):
    contador = 1
    while contador <= valor_max:
        yield contador
        contador += 1


gen = list(conta_ate(10))

print(gen)
