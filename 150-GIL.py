"""
Python GIL (Global Interpreter Lock)

O Python Global Interpreter Lock, ou simplesmente GIL, é um mutex (ou lock) que permite que apenas uma
thread tome conta do interpretador Python.

Isso significa que somente uma thread pode estar em um estado de execução em qualquer ponto do tempo.

O impacto do GIL não é comumente visível para desenvolvedores que executam programas single-thread, mas
pode ser uma dor de cabeça para programas que precisam de tempo de resposta em códigos multi-thread.

Desde que o GIL permite apenas uma thread a ser executada, mesmo em computadores multi-threads com
arquitetura que permite utilizar mais de um CPU ou core, o GIL tem ganhado reputação como um recurso
"indecente" do Python.
"""

import time
from threading import Thread


CONTADOR = 50000000


def contagem_regressiva(n):
    while n > 0:
        n -= 1


inicio = time.time()
contagem_regressiva(CONTADOR)
fim = time.time()

print(f'Tempo em segundos Multi-thread: {fim - inicio}')


# -------------------------------------------
# Single-thread

t1 = Thread(target=contagem_regressiva, args=(CONTADOR//2,))
t2 = Thread(target=contagem_regressiva, args=(CONTADOR//2,))

inicio = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
fim = time.time()

print(f'Tempo em segundos Single-Thread: {fim - inicio}')

# -------------------------------------------
# Multiprocessing - 1.0866985321044922 (collected from MultiProcessing.py)
print(f'Tempo em segundos Multi-Processing: 1.0866985321044922')
