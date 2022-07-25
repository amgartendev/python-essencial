# Testes de Herança, Heranças Múltiplas, Polimorfismo, MRO e Métodos Mágicos


class Animal:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    def cumprimentar(self):
        return f'Eu sou {self.__nome}!'

    def comer(self):
        return f'{self.__nome} está comendo...'


class Terrestre(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, raca)

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da Terra!'

    def andar(self):
        return f'{self._Animal__nome} está andando...'

    def falar(self):
        raise NotImplementedError('Erro: Este método precisa ser implementado!')


class Aereo(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, raca)

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do Ar!'

    def voar(self):
        return f'{self._Animal__nome} está voando...'

    def falar(self):
        raise NotImplementedError('Erro: Este método precisa ser implementado!')


class Aquatico(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, raca)

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do Mar!'

    def nadar(self):
        return f'{self._Animal__nome} está nadando...'

    def falar(self):
        raise NotImplementedError('Erro: Este método precisa ser implementado!')


class Cachorro(Terrestre):
    def __init__(self, nome, raca):
        super().__init__(nome, raca)

    def __str__(self):
        return f'{self._Animal__nome} é Cachorro da raça {self._Animal__raca}'

    def __del__(self):
        print(f'O objeto {self._Animal__nome} foi destruído!')

    def falar(self):
        return f'{self._Animal__nome} fala AU AU!'


class Gato(Terrestre):
    def __init__(self, nome, raca):
        super().__init__(nome, raca)

    def __str__(self):
        return f'{self._Animal__nome} é um Gato da raça {self._Animal__raca}'

    def __del__(self):
        print(f'O objeto {self._Animal__nome} foi destruído!')

    def falar(self):
        return f'{self._Animal__nome} fala MIAU!'


class Passaro(Aereo):
    def __init__(self, nome, raca):
        super().__init__(nome, raca)

    def __str__(self):
        return f'{self._Animal__nome} é um Pássaro da raça {self._Animal__raca}'

    def __del__(self):
        return f'O objeto {self._Animal__nome} foi destruído!'

    def falar(self):
        return f'{self._Animal__nome} fala PIU PIU!'


class Pinguim(Aquatico, Terrestre):
    def __init__(self, nome, raca):
        super().__init__(nome, raca)

    def __str__(self):
        return f'{self._Animal__nome} é um Animal Terrestre e Aquático da raça {self._Animal__raca}'

    def __del__(self):
        print(f'O objeto {self._Animal__nome} foi destruído!')

    def falar(self):
        return f'{self._Animal__nome} fala PINGU!'


cachorro1 = Cachorro('Pluto', 'Dobermann')
print(cachorro1)  # Pluto é Cachorro da raça Dobermann
print(cachorro1.cumprimentar())  # Eu sou Pluto da Terra!
print(cachorro1.comer())
print(cachorro1.andar())
print(cachorro1.falar())

print('=' * 20)

gato1 = Gato('Félix', 'Persa')
print(gato1)  # Félix é um Gato da raça Persa
print(gato1.cumprimentar())  # Eu sou Félix da Terra!
print(gato1.comer())
print(gato1.andar())
print(gato1.falar())

print('=' * 20)

passaro1 = Passaro('Frajola', 'Canário')
print(passaro1)  # Frajola é um Pássaro da raça Canário
print(passaro1.cumprimentar())  # Eu sou Frajola do Ar!
print(passaro1.comer())
print(passaro1.voar())
print(passaro1.falar())

print('=' * 20)

pinguim1 = Pinguim('Pingu', 'Gentoo')
print(pinguim1)  # Pingu é um Animal Terrestre e Aquático da raça Gentoo -- (Herança Múltipla)
print(pinguim1.cumprimentar())  # Eu sou Pingu do Mar! -- MRO (Method Resolution Order)
print(pinguim1.comer())
print(pinguim1.andar())
print(pinguim1.nadar())
print(pinguim1.falar())

print('=' * 20)
print('DELETANDO OS OBJETOS DA MEMÓRIA AO FIM DA EXECUÇÃO')
