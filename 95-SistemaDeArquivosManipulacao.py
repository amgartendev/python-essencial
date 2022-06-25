"""
Sistema de Arquivos - Manipulação

# Descobrindo se um arquivo ou diretório existe

# Arquivo
print(os.path.exists('arquivos.txt'))  # False
print(os.path.exists('frutas.txt'))  # True

# Diretório

# Paths relativos
print(os.path.exists('geek'))  # True
print(os.path.exists('geek/university'))  # True
print(os.path.exists('outro'))  # False

# Paths absolutos
print(os.path.exists('C:\\Users\\rotci\\Desktop\\Code\\GUPPE'))  # True
print(os.path.exists('C:\\Users\\rotci\\Desktop\\Code\\GUPPE\\arquivo.txt'))  # False

# Criando arquivos - Forma menos Utilizada

# Forma 1
open('arquivo-teste.txt', 'w').close()

# Forma 2
open('arquivo-teste2.txt', 'a').close()

# Forma 3
with open('arquivo-teste3.txt', 'w') as arquivo:
    pass


# Criando arquivos - Forma mais Utilizada (Linux)
os.mknod('arquivo-teste4.txt')

os.mknod('C:\\Users\\rotci\\Desktop\\Code\\GUPPE\\university.txt')

# OBS: Se você estiver utilizando no Mac OS, pode haver um erro de PermissionError ou
# se estiver utilizando Windows, pode haver o erro AttributeError

# Criando diretórios

# Path Relativo
os.mkdir('templates')

# Path Absoluto
os.mkdir('C:\\Users\\rotci\\Desktop\\Code\\GUPPE\\templates')

# OBS: A função mkdir() cria um diretório se este não existir. Caso exista, teremos FileExistsError

# OBS: Se não tivermos permissão para criar o diretório teremos um PermissionError

# Criando multi-diretórios (árvore de diretórios)
os.makedirs('templates/geek/university')

# OBS: Se já existir, teremos FileExistsError

os.makedirs('templates/geek/university', exist_ok=True)

# Renomear arquivos e diretórios

# Diretórios
os.rename('templates/geek/university/geek2', 'templates/geek/university/geek3')

# OBS: Se o diretórios não existir teremos um FileNotFoundError

# OBS: Se o diretórios que queremos renomear não estiver vazio, teremos um OSError

# Arquivos
os.rename('templates/geek/university/geek3/geek1.txt', 'templates/geek/university/geek3/geek.txt')

# ATENÇÃO! Tome cuidado com os comandos de deleção. Ao deletarmos um arquivo ou diretórios, eles
# não vão para a lixeira. Eles somem.

# Removendo Arquivos
os.remove('geek.txt')

# OBS: Se você estiver no Windows e o arquivo que você for deletar estiver em uso, você terá um erro.

# OBS: Caso o arquivo não exista, teremos o FileNotFoundError

# OBS: Se você informar um diretório ao invés de um arquivo, teremos um IsADirectoryError

# Removendo diretórios vazios

os.rmdir('templates')

# OBS: Se o diretório tiver qualquer conteúdo teremos um OSError

# OBS: Se o diretório não existir teremos um FileNotFoundError

# Podemos remover uma árvore de diretórios vazios

os.removedirs('geek2/outro/mais')

os.removedirs('geek2/mais')

# Se algum dos diretórios contiver arquivos ou outros diretórios, o processo para.

# Importando a biblioteca send2trash (Envia arquivos e diretórios para a lixeira)
from send2trash import send2trash

os.remove('cesta1.txt')  # Não é enviado para a lixeira. É deletado imediatamente

send2trash('cesta2.txt')  # Vai para a lixeira. Pode ser restaurado

# OBS: Se o arquivo não existir, teremos OSError

send2trash('teste')

# Trabalhando com arquivos e diretórios temporários

import os
import tempfile

# Criando um diretório temporário
with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()

# Estamos criando um diretórios temporário, abrindo o mesmo e dentro dele criando
# um arquivo para escrevermos um texto. No final, usamos um input() só para mantermos
# os arquivos temporários 'vivos' dentro dos blocos with.

# Criando um arquivo temporário

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek Univerisity\n')
    tmp.seek(0)
    print(tmp.read())


# OBS: Em arquivos temporários só conseguimos escrever bytes. Por isso, utilizamos b''

# Sem o bloco with
arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek University\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()


import os
import tempfile


arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek University\n')

print(arquivo.name)

print(arquivo.read())


input()

arquivo.close()

https://docs.python.org/3/library/os.html?highlight=os#module-os
"""
