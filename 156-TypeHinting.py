"""
Type Hinting

É uma solução formal de indicar estáticamente o tipo de um dado em uma linguagem de
programação em que a linguagem de dados é dinâmica.

Se fossemos traduzir, seria algo do tipo "Dica de Tipo"

# Primeiro Exemplo de Type Hinting
def cumprimentar(nome: str) -> str:
    return f'Olá, {nome}'


print(cumprimentar('João'))


# Segundo Exemplo de Type Hinting

def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f'{texto.title()}\n{"-" * len(texto)}'
    else:
        return f' {texto.title()} '.center(50, '#')


print(cabecalho('geek university'))

print(cabecalho('geek university', alinhamento=False))

print(cabecalho('geek university', alinhamento=None))
"""
