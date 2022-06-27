"""
1. Escreva um programa que:
# A -> Crie/Abra um arquivo de texto de nome "arq.txt"
# B -> Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário entre com o caractere '0'
# C -> Feche o arquivo
# Agora, abra e leia o arquivo, caractere por caractere, e escreva na tela todos os caracteres armazenados

with open('arq.txt', 'w') as arq:
    while True:
        user = input('>>> ')
        if user == '0':
            break
        arq.write(user)

with open('arq.txt', 'r') as arq:
    print(arq.read())
"""


"""
2. Faça um programa que receba do usuário um arquivo de texto e mostre na tela quantas linhas
esse arquivo possui.

user = input('>>> ')

with open(user, 'r') as arq:
    print(len(arq.readlines()))
"""


"""
3. Faça um programa que receba do usuário um arquivo de texto e mostre na tela quantas letras
são vogais.

contagem = 0
vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

user = input('>>> ')

with open(user, 'r') as arq:
    for palavra in arq.readlines():
        for letra in palavra:
            if letra in vogais:
                contagem += 1

print(contagem)
"""


"""
4. Faça um programa que receba do usuário um arquivo de texto e mostre na tela quantas letras
são vogais e quantas são consoantes.

contagem_vogais = 0
contagem_consoantes = 0

vogais = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

user = input('>>> ')

with open(user, 'r') as arq:
    for palavra in arq.readlines():
        for letra in palavra:
            if letra not in vogais and letra.isalpha():
                contagem_consoantes += 1
            if letra in vogais and letra.isalpha():
                contagem_vogais += 1

print(contagem_consoantes)
print(contagem_vogais)
"""


"""
5. Faça um programa que receba do usuário um arquivo texto e caractere. Mostre na tela quantas vezes
aquele caractere ocorre dentro do arquivo.

user_file = input('>>> ')
user_char = input('>>> ')

count = 0

with open(user_file, 'r') as f:
    for word in f.readlines():
        for char in word:
            if char == user_char:
                count += 1

print(count)
"""


"""
6. Faça um programa que receba do usuário um arquivo de texto e mostre na tela quantas vezes cada letra
do alfabeto aparece dentro do arquivo.

alphabet = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
            'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
            'y': 0, 'z': 0}


user_file = input('>>> ')

with open(user_file, 'r') as f:
    for word in f.readlines():
        for char in word:
            if char != ' ' and char.isalpha():
                alphabet[char] += 1

print(alphabet)
"""


"""
7. Faça um programa que receba do usuário um arquivo texto. Crie outro arquivo de texto contendo o texto
do arquivo de entrada, mas com as vogais substituídas por '*'.

vogais = ['a', 'e', 'i', 'o', 'u']

user_file = input('>>> ')

with open(user_file, 'r+') as file:
    with open(f'{user_file}2', 'w') as new_file:
        for word in file.readlines():
            for char in word:
                if char in vogais:
                    new_file.write(char.replace(word[word.index(char)], '*'))
                else:
                    new_file.write(char)
"""


"""
8. Faça um programa que leia o conteúdo de um arquivo e crie um arquivo com o mesmo conteúdo mas com todas
as letras minúsculas convertidas para maiúsculas. Os nomes dos arquivos serão fornecidos, via teclado, pelo
usuário. A função que converte minúscula para maiúscula é upper(). Ela é aplicada em cada caractere da 
string.

user_open_file = input('>>> ')
user_new_file = input('>>> ')

with open(user_open_file, 'r') as old_file:
    with open(user_new_file, 'w') as new_file:
        for word in old_file.readlines():
            new_file.write(word.upper())
"""


"""
9. Faça um programa que receba dois arquivos do usuário, e crie um terceiro arquivo com o conteúdo dos dois
primeiros juntos (o conteúdo do primeiro seguido do conteúdo do segundo).

user_file1 = input('>>> ')
user_file2 = input('>>> ')


with open('result.txt', 'w') as result:
    with open(user_file1, 'r') as file1:
        with open(user_file2, 'r') as file2:
            result.write(file1.readline() + file2.readline())
"""


"""
10. Faça um programa que receba o nome de um arquivo de entrada e outro de saída. O arquivo de entrada
contém em cada linha o nome de uma cidade (ocupando 40 caracteres) e o seu número de habitantes. O
programa deverá ler o arquivo de entrada e gerar um arquivo de saída onde aparece o nome da cidade
mais populosa seguida pelo seu número de habitantes.

------------ N FEITO ------------
"""


"""
11. Faça um programa no qual o usuário informe o nome do arquivo e uma palavra, e retorna
o número de vezes que aquela palavra aparece no arquivo.

user_file = input('>>> ')
word = input('>>> ')

with open(user_file, 'r') as file:
    list_words = file.readline()
    list_words.split(',')
    print(list_words.count(word))
"""


"""
12. Abra um arquivo de texto, calcule e escreva o número de caracteres, o número de linhas e o
número de palavras neste arquivo. Escreva também quantas vezes cada letra ocorre no arquivo
(ignorando letras com acento). Obs.: palavras são separadas por um ou mais caracteres de espaço,
tabulação ou nova linha.

from collections import Counter

with open('arq.txt', 'r', encoding='UTF-8') as file:
    count_words = 0
    count_chars = 0

    lines = file.readlines()

    for word in lines:
        count_words += 1
        for char in word:
            count_chars += 1
    file.seek(0)

    print(f'Caracteres: {count_chars}')
    print(f'Linhas: {len(lines)}')
    print(f'Palavras: {count_words}')
    print(f'Ocorrencia de caracteres: {Counter(file.read())}')
"""


"""
BONUS: Faça um programa que receba do usuário um arquivo de texto e mostre na tela quantas vezes cada 
caractere aparece dentro do arquivo.

from collections import Counter

user_file = input('>>> ')

with open(user_file, 'r') as f:
    res = f.read()
    print(Counter(res))
"""
