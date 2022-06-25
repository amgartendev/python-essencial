"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar
e fazer uso do módulo os.

os -> Operating System - Sistema Operacional


# Fazendo o import
import os

# getcwd() -> Get Current Working Directory - Pegar o diretório atual
# Retorna o path (caminho) absoluto
print(os.getcwd())  # C:\\Users\\rotci\\Desktop\\Code\\GUPPE

# Para mudar o diretório, podemos utilizar o chdir()

os.chdir('..')

print(os.getcwd())  # C:\\Users\\rotci\\Desktop\\Code

os.chdir('..')

print(os.getcwd())  # C:\\Users\\rotci\\Desktop

os.chdir('..')

print(os.getcwd())  # C:\\Users\\rotci

os.chdir('..')

print(os.getcwd())  # C:\\Users

os.chdir('..')

print(os.getcwd())  # C:\\


# Se quisermos ir para a raíz mais rápido, também podemos fazer:

while os.getcwd() != 'C:\\':
    os.chdir('..')
    print(os.getcwd())


# Podemos chegar se um diretório é absoluto ou relativo

print(os.path.isabs('/home/rotci'))  # True

# OBS: Para usuários Windows
# Se você, infelizmente, estiver utilizando um computador com Windows,
# terá que ter cuidado ao verificar diretórios.

print(os.path.isabs('C:\\Users\\rotci'))  # True

# Podemos identificar o sistema operacional com o módulo os
print(os.name)  # posix (Linux e Mac), nt (Windows)

# Podemos ter mais detalhes no sistema operacional
print(os.uname())  # Funciona apenas em sistemas UNIX

# Caso estejamos no Windows
import platform

print(platform.uname())



print(os.getcwd())  # C:\\Users\\rotci\\Desktop\\Code\\GUPPE

res = os.path.join(os.getcwd(), 'geek', 'university')

os.chdir(res)

print(os.getcwd())  # C:\\Users\\rotci\\Desktop\\Code\\GUPPE\\geek\\university

# Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro o diretório atual e o segundo o
# diretório que será juntado ao atual.

# Podemos listar os arquivos e os diretórios com o listdir()

print(os.listdir())

# Podemos listar os arquivos e os diretórios com o listdir() passando parâmetros do diretório que queremos

print(os.listdir('geek'))

# Podemos listar os arquivos e diretórios com mais detalhes com scandir()

print(list(os.scandir('geek')))

"""

# Fazendo o import
import os

scanner = os.scandir()

arquivos = list(scanner)

# print(arquivos)

# print(dir(arquivos[0]))


print(arquivos[0].inode())  # Identificador do arquivo
print(arquivos[0].is_dir())  # É um diretório? False
print(arquivos[0].is_file())  # É um arquivo? True
print(arquivos[0].is_symlink())  # É um link simbólico? False
print(arquivos[0].name)  # Nome do arquivo
print(arquivos[0].path)  # Caminho até o arquivo
print(arquivos[0].stat())  # Estatísticas sobre arquivo

# OBS: Quando utilizamos a função scandir() nós precisamos fechá-la, assim quando abrimos um arquivo.

scanner.close()
