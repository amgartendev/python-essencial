"""
Alerta Sobre Sintaxes Perigosas

Nós estamos acostumados a receber mensagens de SyntaxError quando erramos alguma syntax no nosso programa.
Mas, nas novas versão do Python, também temos a SyntaxWarning. É um alerta que é mostrado quando a nossa
syntax não está errada, mas pode causar algum perigo em algumas situações.

Por exemplo:
É comum alguns desenvolvedores confundirem o uso do 'is' com o '=='

== -> Usado para checar valor
is -> Usado para checar se os objetos são os mesmos

# Python 3.7 no Terminal
versao = '3.7'
versao is '3.7' -> Nos retorna False

# Esquecendo uma vírgula propositalmente
lista = [('Shizo')('Tom')] -> TypeError: 'str' object is not callable


# Python 3.8 no Terminal

versao = '3.8'
versao is '3.8' -> <stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="? False
versao == '3.8' -> True

# Esquecendo uma vírgula propositalmente
lista = [('Shizo')('Tom')] -> <stdin>:2: SyntaxWarning: 'str' object is not callable; perhaps you missed a comma?
"""
