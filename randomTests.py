def soma():
    soma = 0

    try:
        numero = int(input())
        for numero in str(numero):
            soma += int(numero)
        return soma

    except ValueError as valueErrorMsg:
        return f'An error has occured: {valueErrorMsg}'
