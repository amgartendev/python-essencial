# Herança e Polimorfismo


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.__nome = nome
        self.__sobrenome = sobrenome

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def cumprimentar(self):
        return f'{self.__nome} está te cumprimentando!'


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, numero_cliente):
        super().__init__(nome, sobrenome)
        self.__numero_cliente = numero_cliente

    def cumprimentar(self):
        return f'Olá, eu sou o cliente {self._Pessoa__nome}'


class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, licenca):
        super().__init__(nome, sobrenome)
        self.__licenca = licenca

    def cumprimentar(self):
        return f'Olá, eu sou o funcionário {self._Pessoa__nome}'


cliente1 = Cliente('Fulano', 'Ciclano', 'BA321')
print(cliente1.nome_completo())
print(cliente1.cumprimentar())

funcionario1 = Funcionario('Joao', 'Amgarten', 'AB123')
print(funcionario1.nome_completo())
print(funcionario1.cumprimentar())

print(funcionario1)
