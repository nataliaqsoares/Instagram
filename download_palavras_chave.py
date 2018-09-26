""" Problema:
Criar um script que baixe as 20 palavras chaves que mais são usadas no instagram @christiantriad """

import instaloader
import glob
import os
import collections

""" Baixa os arquivos do perfil """

# Inicia a biblioteca
loader = instaloader.Instaloader()

# Informa de qual perfil os dados serão coletados
profile = instaloader.Profile.from_username(loader.context, 'christiantriad')

# Baixa todos os posts do perfil
for post in instaloader.Profile.get_posts(profile):
    # Faz o download dos posts e cria a pasta onde serão salvos
    loader.download_post(post, target=profile.username)

""" Separa o conteudo que a ser usado """

# Escreve na tela
print('=' * 10)
print('Filtrando as palavras a serem usadas....')
print('=' * 10)

# Cria o arquivo onde as legendas das imagens serão escritos
palavras = open(os.path.join('palavras.txt'), 'w')

# Lista onde os arquivos a serem lidos estão
os.chdir('C:\\Users\\Natália\\Desktop\\Instagram\\christiantriad')
# Lista todos os arquivos .txt
for file in glob.glob('*.txt'):
    # Tira os arquivos com final _location.txt
    if file not in glob.glob('*_location.txt'):
        # Abre o arquivo para que possa ser lido e ignora os erros de codificação
        abrir_arquivo = open(file, errors='ignore')
        # Le o conteudo dos arquivos
        recebe_conteudo = abrir_arquivo.read()
        # Escreve o conteudo dos arquivos e no final faz uma quebra de linha
        palavras.write(recebe_conteudo + '\n')

""" Conta as palavras-chave """

# Escreve na tela
print('=' * 10)
print('Contando as palavras chave....')
print('=' * 10)

# Inicia o contador
contador = collections.Counter()
# Lista os arquivos a serem lidos
os.chdir('C:\\Users\\Natália\\Desktop\\Instagram')
# Abre o arquivo onde estão todas as palavras das legendas das imagens
abrir_arquivo_2 = open(os.path.join('palavras.txt'))
# Le o counteudo do arquivo anterior
recebe_conteudo_2 = abrir_arquivo_2.read()
# Separa o conteudo em palavras
for palavra in recebe_conteudo_2.split():
    # Filtra as palavras que começam com #
    if '#' in palavra:
        # Conta cada palavra
        contador.update(palavra.split())

""" Escreve os resultados em um arquivo """

# Escreve na tela
print('=' * 10)
print('Salvando as 20 palavras chave mais usadas....')
print('=' * 10)

# Cria onde os resultados serão escritos
palavras_chave = open(os.path.join('palavras_chave.txt'), 'w')
# Escreve os 20 maiores resultados (palavras-chave mais usadas)
palavras_chave.write(str(contador.most_common(20)))
