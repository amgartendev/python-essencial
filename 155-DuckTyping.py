"""
Duck Typing

Sim... Duck de pato, pato... Quack Quack... pato

O Duck Typing está relacionado com a tipagem dinâmica de dados. O tipo ou a classe de objeto
é menos importante que os métodos que o definem.

Se determinado objeto se parece com um pato, anda como um pato e nada como um pato. É um pato.
Daí o nome Duck Typing.

Objetos similares devem ter métodos, atributos e comportamentos similares. Se existe um
objeto que é similar a outro, possívelmente deve ter o mesmos métodos, atributos e
comportamentos igual ao outro.
"""


class CisneNegro:

    def __len__(self):
        return 42


livro = CisneNegro()

print(len(livro))

nome = 'Geek University'
lista = [12, 34, 55, 49]
dicio = {"carlos": 12, "vanessa": 34, "joana": 49}

print(len(nome))
print(len(lista))
print(len(dicio))

idade = 42
peso = 81.4

# print(len(idade))  # Erro. Int não possui o método len()
