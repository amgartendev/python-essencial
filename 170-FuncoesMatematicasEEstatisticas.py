"""
Funções Matemáticas e Estatísticas

Dentro do módulo math nós temos vários outros métodos ainda não estudados, como:

math.prod - Retorna o produto de um container númerico
math.isqrt - Retorna o valor inteiro de uma raíz quadrada
math.dist - Retorna a distância euclidiana entre dois pontos, seja os pontos 2D ou 3D
math.hypot - Retorna a hipotenusa, ou norma Euclidiana

Dentro do módulo statistics nós também temos:
statistics.fmean - Retorna o cálculo da média de números reais
statistics.geometric_mean - Retorna o cálculo da média geométrica de números reais
statistics.multimode - Retorna o valor mais frequente em uma sequência


import math

# math.prod

nums_v1 = [2, 4, 6, 8]
nums_v2 = (2, 3, 6, 8)
nums_v3 = {2, 3, 6, 8}

print(math.prod(nums_v1))  # 2 * 4 * 6 * 8 = 384
print(math.prod(nums_v2))  # 2 * 3 * 6 * 8 = 288
print(math.prod(nums_v2))  # 2 * 3 * 6 * 8 = 288


# math.isqrt vs math.sqrt

print(math.isqrt(9))
print(math.sqrt(9))
print(math.isqrt(17))
print(math.sqrt(17))


# math.dist

# Pontos 2D
ponto2D1 = [12, 50]
ponto2D2 = [6, 7]

# Pontos 3D
ponto3D1 = (12, 50, 40)
ponto3D2 = (6, 7, 13)

print(math.dist(ponto2D1, ponto2D2))
print(math.dist(ponto3D1, ponto3D2))


# math.hypot

print(math.hypot(*ponto2D1))  # Descompactando a lista com *
print(math.hypot(*ponto3D1))  # Descompactando a tupla com *


import statistics

# Estatística

# statistics.fmean

valores_reais = [1.45, 6.789, 3.45, 89.98765]
valores_inteiros = [1, 6, 3, 89]

print(statistics.fmean(valores_reais))
print(statistics.fmean(valores_inteiros))

# O fmean sempre vai nos devolver a média em números reais convertendo todos os números
# para números reais, mesmo se passarmos números inteiros


# statics.geometric_mean

valores_reais = [1.45, 6.789, 3.45, 89.98765]
valores_inteiros = [1, 6, 3, 89]

print(statistics.geometric_mean(valores_reais))
print(statistics.geometric_mean(valores_inteiros))


# statistics.multimode

sequencia1 = 'Uma sequência em string'
sequencia2 = [3, 5, 3, 8, 7, 9, 5, 3]
sequencia3 = [1, 2, 3, 1, 2, 3, 4, 5, 6]

print(statistics.multimode(sequencia1))
print(statistics.multimode(sequencia2))
print(statistics.multimode(sequencia3))
"""
import statistics

# statistics.multimode

sequencia1 = 'João Amgarten'
sequencia2 = [3, 5, 3, 8, 7, 9, 5, 3]
sequencia3 = [1, 2, 3, 1, 2, 3, 4, 5, 6]

print(statistics.multimode(sequencia1))
print(statistics.multimode(sequencia2))
print(statistics.multimode(sequencia3))
