"""
Checagem de Tipos com MyPY

http://mypy-lang.org

# pip install mypy

Para executarmos a verificação de tipos com o MyPy devemos abrir o terminal
e executar: mypy nome_do_modulo.py

OBS: Para execurtamos o MyPy, devemos usar o Type Hinting, caso contrário,
o MyPy não acusará nenhum erro, mas com o código escrito de forma errada.

# Exemplo - FUNCIONAL

# Usando Type Hinting
def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f'{texto.title()}\n{"-" * len(texto)}'
    else:
        return f' {texto.title()} '.center(50, '#')


print(cabecalho('geek university'))

print(cabecalho('geek university', alinhamento=False))

# print(cabecalho('geek university', alinhamento=None))
print(cabecalho('geek university', alinhamento=True))


# Exemplo - ERRADO

# Não utilizando Type Hinting
def cabecalho(texto, alinhamento=True):
    if alinhamento:
        return f'{texto.title()}\n{"-" * len(texto)}'
    else:
        return f' {texto.title()} '.center(50, '#')


print(cabecalho('geek university'))

print(cabecalho('geek university', alinhamento=False))

# print(cabecalho('geek university', alinhamento=None))
print(cabecalho('geek university', alinhamento=True))
"""



