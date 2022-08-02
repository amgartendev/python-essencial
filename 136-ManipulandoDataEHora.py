"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora
chamado datetime

2022-08-02 18:29:05.891569

2022-08-02 18:34:05.891569

# print(dir(datetime))

print(datetime.MAXYEAR)

print(datetime.MINYEAR)


# Retorna a data e hora atual

print(datetime.datetime.now())  # 2022-08-02 18:29:05.891569


# datetime.datetime(year, month, day, hour, minute, seconds, microseconds)
print(repr(datetime.datetime.now()))

# replace() para fazer ajustes na data/hora

inicio = datetime.datetime.now()

print(inicio)

# Alterar o horário para 16 horas, 0 minuto, 0 segundo, 0 microsegundo para o ano de 2023
inicio = inicio.replace(year=2023, hour=16, minute=0, second=0, microsecond=0)

print(inicio)

# Recebendo dados do usuário e convertendo para data

evento = datetime.datetime(2019, 1, 1, 0)

print(type(evento))

print(type('31/12/2018'))


print(evento)


nascimento = input('Informe sua data de nascimento (dd/mm/yyyy): ')

nascimento = nascimento.split('/')

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)

print(type(nascimento))
"""

import datetime


evento = datetime.datetime.now()


# Acesso individual dos elementos de data e hora

print(evento.year)  # Ano
print(evento.month)  # Mês
print(evento.day)  # Dia
print(evento.hour)  # Hora
print(evento.minute)  # Minuto
print(evento.second)  # Segundo
print(evento.microsecond)  # Microsegundo

print(dir(evento))
