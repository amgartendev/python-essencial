"""
Trabalhando com deltas de data e hora

data_inicial = dd/mm/yyyy 12:55:34:328101
data final = dd/mm/yyyy   13:34:23:417412

delta = data_final - data_inicial

import datetime

# Temos a data de hoje
data_hoje = datetime.datetime.now()

# Data para ocorrer um determinado evento no futuro
data_aniversario = datetime.datetime(2022, 12, 16)

# Calculando o Delta
tempo_para_evento = data_aniversario - data_hoje

print(type(tempo_para_evento))

print(repr(tempo_para_evento))

print(tempo_para_evento)

print(f'Faltam {tempo_para_evento.days} dias, {tempo_para_evento.seconds//60//60} horas...')
"""

import datetime

data_da_compra = datetime.datetime.now()

print(data_da_compra)

regra_boleto = datetime.timedelta(days=3)

print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto

print(vencimento_boleto)
