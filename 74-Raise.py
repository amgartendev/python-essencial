"""
Levantando os próprios erros com Raise

raise -> Lança exceções

OBS: O Raise não é uma função. É uma palavra reservada, assim como def ou qualquer outra em Python.

Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias exceções e mensagens
de erro.

A forma geral  de utilização é:

raise TipoDoErro('Mensagem de Erro')

# Exemplo Real

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string!')

    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string!')

    return f'O texto {texto} será impresso na cor {cor}'


print(colore('True', 'azul'))


# Exemplo Refatorado

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string!')

    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string!')

    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}!')

    return f'O texto {texto} será impresso na cor {cor}'


print(colore('Geek University', 'preto'))

OBS: O raise, assim como o return, finaliza a função. Ou seja, nada após o raise é executado.
"""

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string!')

    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string!')

    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}!')

    return f'O texto {texto} será impresso na cor {cor}'


print(colore('Geek University', 'preto'))