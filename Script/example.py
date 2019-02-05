#Le o arquivo, escreve do tamanho passado por parametro 'song.read(2)', ele escreve 2 caracters do arquivo
# Se você entra com um argumento do tipo inteiro no método read, ele é lido até atingir aquele número de caracteres,
# retorna todos eles e mantém a "janela" naquela posição, pronta para continuar lendo.

with open('camelot.txt') as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())

#Le uma Linha do arquivo
with open('camelot.txt') as song:
    print(song.readline())