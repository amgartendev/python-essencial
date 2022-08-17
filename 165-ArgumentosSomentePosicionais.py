"""
Argumento somente posicionais

# help(float())
# class float(object):
    float(x=0, /)
    ...

Podemos notar que existe um parâmetro 'x' em float e uma '/'.
O que isso significa?
    - O x já conhecemos, é um parâmetro padrão.
    - A / indica que aquele x é um argumento somente posicional

Quando temos um argumento somente posicional não podemos indicar X na execução da função.
Por exemplo:
print(float(x=5.45))  # TypeError: float() got some positional-only arguments passed as keyword arguments: 'x'

Com argumentos posicionais, qualquer valor que for inserido como argumento, irá ser atribuído
para o aquele parâmetro padrão. No caso do float(), o x.


def cumprimenta_v1(nome):
    return f'Olá {nome}'


print(cumprimenta_v1('João'))
print(cumprimenta_v1(nome='João'))


def cumprimenta_v2(nome, /):
    return f'Olá {nome}'

print(cumprimenta_v2('João'))
print(cumprimenta_v2(nome='João'))  # TypeError: cumprimenta_v2() got some positional-only arguments passed as keyword arguments: 'nome'

def cumprimenta_v3(nome, /, mensagem='Olá'):
    return f'{mensagem} {nome}'


print(cumprimenta_v3('João'))
print(cumprimenta_v3('Thiago', mensagem='Hello'))
print(cumprimenta_v3('Felicity', mensagem='Bem-vinda'))


# Se quisermos passar múltiplos argumentos posicionais, posicionamos a '/' no fim


def cumprimenta_v4(nome, mensagem='Olá', /):
    return f'{mensagem} {nome}'


print(cumprimenta_v4('João'))
print(cumprimenta_v4('Felicity', 'Bem-vinda'))
print(cumprimenta_v4('Thiago', mensagem='Hello'))  # TypeError: cumprimenta_v4() got some positional-only arguments passed as keyword arguments: 'mensagem'

# Também podemos fazer com que TODOS os argumentos após o '*' devem ser OBRIGATÓRIAMENTE informados


def cumprimenta_v5(*, nome):
    return f'Olá {nome}'


print(cumprimenta_v5(nome='João'))
print(cumprimenta_v5('João'))  # TypeError: cumprimenta_v5() takes 0 positional arguments but 1 was given
"""


def cumprimentar_v6(nome, /, mensagem1='Olá', *, mensagem2):
    return f'{mensagem1} {nome} {mensagem2}'


print(cumprimentar_v6('João', mensagem1='Hello', mensagem2='tenha um bom dia'))
print(cumprimentar_v6('Michelle', mensagem2='tenha um bom dia'))
print(cumprimentar_v6('John', 'Oi', 'Vamos?'))  # TypeError: cumprimentar_v6() takes from 1 to 2 positional arguments but 3 were given

