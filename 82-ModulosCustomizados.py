"""
Módulos Customizados

Como módulos Python nada mais são do que arquivos Python, então TODOS os arquivos que criamos
neste curso são módulos Python prontos para serem utilizados.

# Importando uma função específica do nosso módulo
from modulos import soma_todos_numeros

print(soma_todos_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9))

# Importando todo o módulo (Temos acesso a TODOS os elementos do módulo)
import modulos

# Estamos acessando e imprimindo uma variável contida no módulo
print(modulos.lista)

print(modulos.tupla)

print(modulos.soma_impares(modulos.lista))
"""

from modulos import cidades, c_para_f

print(list(map(c_para_f, cidades)))
