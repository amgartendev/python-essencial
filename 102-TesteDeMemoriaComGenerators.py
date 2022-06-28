"""
Teste de Memória com Generators

# Sequência de Fibonacci
1 1 2 3 5 8 13 21...


# Função usando listas 470MB

def fib_list(max_num):
    nums = []
    a, b = 0, 1
    while len(nums) < max_num:
        nums.append(b)
        a, b = b, a + b
    return nums


# Teste 1
for n in fib_list(100000):
    print(n)


# Função usando Generators 4.8MB


def fib_list_generator(max_num):
    a, b, contador = 0, 1, 0

    while contador < max_num:
        a, b = b, a + b
        yield a
        contador += 1


# Teste 2
for n in fib_list_generator(100000):
    print(n)
"""
