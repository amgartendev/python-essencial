"""
O bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo
assim que nosso programa pare de funcionar e o usuário receba mensagens de erros inesperadas.

A forma geral mais simples é:

try:
    # Execução problemática
except:
    # O que deve ser feito em caso de problema


# Exemplo 1 - Tratando um erro genérico

try:
    geek()
except:
    print('Deu algum problema')

# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro.


# Exemplo 2 - Tratando erro genérico

try:
    len(5)
except:
    print('Deu algum problema')

# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro.

OBS: Tratar erro de forma genérica não é uma boa prática. O ideal é SEMPRE
tratar de forma específica.


# Exemplo 3 - Tratando um NameError

try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente!')


# Exemplo 4 - Tratando um TypeError

try:
    len()
except TypeError:
    print('Você está utilizando um tipo de dado inválido!')


# Exemplo 5 - Tratando um TypeError com mensagem de erro detalhada

try:
    len()
except TypeError as error:
    print(f'A aplicação gerou o seguinte erro: {error}')


# Podemos efetuar diversos tratamentos de erros de uma vez.

try:
    # len(5)
    geek()
    #print('Geek'[9])
    
except NameError as nameErrorMsg:
    print(f'Deu NameError: {nameErrorMsg}')

except TypeError as typeErrorMsg:
    print(f'Deu TypeError: {typeErrorMsg}')

except:
    print('Deu um erro diferente!!')
"""


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]

    except KeyError as keyErrorMsg:
        return f'Chave inexistente: {keyErrorMsg}'

    except TypeError as typeErrorMsg:
        return f'Erro de tipo de dado: {typeErrorMsg}'


dic = {'nome': 'Geek'}
print(pega_valor(dic, "nome"))
