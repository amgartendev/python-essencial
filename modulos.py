lista = [1, 2, 3, 4, 5, 6, 7]

tupla = (1, 2, 3, 4, 5, 6, 7)

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova Iorque', 28), ('Londres', 22)]

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)


def soma_todos_numeros(*args):
    return sum(args)


def soma_impares(numeros):
    total = 0
    for numero in numeros:
        if numero % 2 != 0:
            total += numero
    return total


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares(lista))

    tupla = (1, 2, 3, 4, 5, 6, 7)
    print(soma_impares(tupla))
