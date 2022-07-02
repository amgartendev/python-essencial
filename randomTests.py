from functools import wraps


def gritar(funcao):
    """Retorna a função pedindo_comida tudo em maiúscula"""
    @wraps(funcao)
    def gritando(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return gritando


@gritar
def pedindo_comida(principal, acompanhamento):
    """Retorna um texto pedindo a comida"""
    return f'Quero pedir uma {principal} com {acompanhamento}'


print(pedindo_comida('Picanha', 'Batata Frita'))
print(f'Nome: {pedindo_comida.__name__}')
print(f'Docs: {pedindo_comida.__doc__}')
