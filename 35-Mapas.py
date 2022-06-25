import random

opcoes = ['pedra', 'papel', 'tesoura']

escolher = random.choice(opcoes)

usuario = str(input('Insira PEDRA/PAPEL/TESOURA: ')).lower()

if usuario == 'pedra' and escolher == 'papel':
    print('VOCE PERDEU')
elif usuario == 'papel' and escolher == 'tesoura':
    print('VOCE PERDEU')
elif usuario == 'tesoura' and escolher == 'pedra':
    print('VOCE PERDEU')
elif usuario == escolher:
    print('EMPATE')
else:
    print('VOCE GANHOU')
