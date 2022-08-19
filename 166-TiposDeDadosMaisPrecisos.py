"""
Tipos de dados mais precisos

Já conhecemos
    - int;
    - str;
    - float;
    - list;
    - set;
    - dict;
    - etc.

Nas novas versões do Python temos também
    - Literal;
    - Union;
    - Final;
    - Typed dictionaries;
    - Protocols.


# Literal Type

from typing import Literal


# Literal -> Retorna a string 'conectado' OU 'desconectado'
def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
    pass


# Sem o Literal Type
def calcula_v1(operacao: str, num1: int, num2: int) -> None:
    match operacao:
        case '+':
            print(f'{num1} + {num2} = {num1 + num2}')
        case '-':
            print(f'{num1} - {num2} = {num1 - num2}')
        case _:
            # !r faz com que o parâmetro passado seja informado dentro de aspas simples na mensagem de erro
            raise ValueError(f'Operação inválida {operacao!r}')


calcula_v1('+', 6, 4)
calcula_v1('-', 10, 2)
calcula_v1('*', 3, 5)


# Com o Literal Type
def calcula_v2(operacao: Literal['+', '-'], num1: int, num2: int) -> None:
    match operacao:
        case '+':
            print(f'{num1} + {num2} = {num1 + num2}')
        case '-':
            print(f'{num1} - {num2} = {num1 - num2}')
        case _:
            # !r faz com que o parâmetro passado seja informado dentro de aspas simples na mensagem de erro
            raise ValueError(f'Operação inválida {operacao!r}')

# Podemos escolher qual dado o usuário deverá escolher usando o Literal nos parâmetros de uma função


calcula_v2('+', 6, 4)
calcula_v2('-', 10, 2)
calcula_v2('*', 3, 5)


# Union
def soma(num1: int, num2: int) -> Union[str, int]:
    resultado: int = num1 + num2

    if resultado > 50:
        return f'O valor {resultado} é muito grande'
    return resultado


# Final

from typing import Final

NOME: Final = 'Amgarten'

print(NOME)

NOME = 'John'  # MyPy: Cannot assign to final name "NOME"

print(NOME)


# Também temos o decorador final
from typing import final


# Quando utilizamos o decorador @final em uma classe ou método, nenhuma outra classe pode extender dela.
@final
class Pessoa:
    pass


class Estudante:
    pass

    @final
    def estudar(self):
        print('Estou estudando...')


class Estagiario(Estudante):
    pass

    def estudar(self):
        print('Estudando e estagiando...')


# Typed Dictionaries

from typing import TypedDict


class CursoPython(TypedDict):
    versao: str
    atualizacao: int


curso = CursoPython(versao='3.8.5', atualizacao=2022)
print(curso)

outro = CursoPython(algo='vai', coisa='True')  # MyPy: Extra keys ("algo", "coisa") for TypedDict "CursoPython"
print(outro)
"""

# Protocols

from typing import Protocol


class Curso(Protocol):
        titulo: str


def estudar(valor: Curso) -> None:
    print(f'Estou estudando o curso {valor.titulo}')


class Venda:
    titulo = 'Oi'


v1 = Venda()
# c1 = Curso()


# estudar(c1)
estudar(v1)
