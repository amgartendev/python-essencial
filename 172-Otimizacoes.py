"""
Otimizações

A cada versão nova lançada no Python ocorre uma melhoria no gerenciamento de memória
e na otimização das versões antigas. Podemos ver isso com dois exemplos no Terminal


# Python 3.7 no Terminal
import collections
from timeit import timeit

Pessoa = collections.namedtuple('Pessoa', 'nome email')
felicity = Pessoa('Felicity Jones',  'felicity@gmail.com')

print(timeit('felicity.email', globals=globals())) -> 0.05854409199957106


# Python 3.8 no Terminal
import collections
from timeit import timeit

Pessoa = collections.namedtuple('Pessoa', 'nome email')
felicity = Pessoa('Felicity Jones',  'felicity@gmail.com')

print(timeit('felicity.email', globals=globals())) -> 0.02983354400069715

Globals nos mostra as variáveis globais do nosso ambiente
"""
