"""
Tipagem Dinâmica e Estática

A linguagem Python utiliza uma tipagem dinâmica, o que significa que para atribuirmos algum dado
a uma variável, é necessário apenas informar o dado da variável. A checagem do tipo do dado é
feito apenas na hora da execução do nosso código.

idade = 42

print(type(idade))  # int

idade = 'Quarenta e Dois'

print(type(idade))  # string


# Pelo fato da checagem ser feita apenas na execução do nosso código, temos um problema.

if True:
    resultado = 1 + 'Geek'
else:
    resultado = 1 + 41

print(resultado)

# O código irá quebrar pelo fato de não conseguirmos somar uma inteiro a uma string, mas
# o nosso código não nos fala que é uma operação impossível de ser realizada até executarmos
# o programa. Esse é o problema de linguagens com tipagem dinâmica.
"""
