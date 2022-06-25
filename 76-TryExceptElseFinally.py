"""
Try / Except / Else / Finally

Dica de quando e onde tratar código:

TODA ENTRADA DEVE SER TRATADA!

OBS: A função do usuário é DESTRUIR seu sistema.

# Else -> É executado somente se não ocorrer o erro.

try:
    num = int(input('Informe um número: '))
except ValueError as valueErrorMsg:
    print(f'Valor incorreto: {valueErrorMsg}')
else:
    print(f'Você digitou {num}')

# Finally 

try:
    num = int(input('Informe um número: '))
except ValueError as valueErrorMsg:
    print(f'Valor incorreto: {valueErrorMsg}')
else: 
    print(f'Você digitou o número {num}')
finally:
    print('Executando o finally!')


# OBS: O bloco finally é SEMPRE executado. Independente se houve exceção ou não.

# O finally, geralmente, é utilizado para fechar ou desalocar recursos.

# Exemplos mais complexo ERRADO

def dividir(x, y):
    return x / y


try:
    num1 = int(input('Informe o primeiro número: '))
    num2 = int(input('Informe o segundo número: '))
except ValueError as valueErrorMsg:
    print('O valor precisa ser númerico!')
else:
    print(dividir(num1, num2))


# Exemplos mais complexo CORRETO
# OBS: Você é responsável pelas entradas das suas funções. Então trate-as.


def dividir(x, y):
    try:
        return int(x) / int(y)
    except ValueError:
        return 'Valor incorreto!'
    except ZeroDivisionError:
        return 'Não é possível dividir por zero!'

    
num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))


# Exemplos mais complexo - Genérico
# OBS: Você é responsável pelas entradas das suas funções. Então trate-as.


def dividir(x, y):
    try:
        return int(x) / int(y)
    except:
        return 'Ocorreu um erro!'

    
num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))


# Exemplos mais complexo - Semi-Genérico
# OBS: Você é responsável pelas entradas das suas funções. Então trate-as.


def dividir(x, y):
    try:
        return int(x) / int(y)
    except (ValueError, ZeroDivisionError) as error:
        return f'Ocorreu um erro: {error}'

    
num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))
"""

