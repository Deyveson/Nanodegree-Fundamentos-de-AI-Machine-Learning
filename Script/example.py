# # Todo: Le o arquivo, escreve do tamanho passado por parametro 'song.read(2)', ele escreve 2 caracters do arquivo
# # Se você entra com um argumento do tipo inteiro no método read, ele é lido até atingir aquele número de caracteres,
# # retorna todos eles e mantém a "janela" naquela posição, pronta para continuar lendo.
#
# with open('camelot.txt') as song:
#     print(song.read(2))
#     print(song.read(8))
#     print(song.read())
#
# # Todo: Lendo linha por linha
# # \n em blocos de texto são caracteres indicando uma nova linha. O caractere de nova linha marca o final de uma linha e diz
# # para um programa (como um editor de texto) passar para a próxima linha. No entanto, olhando para o fluxo de caracteres no arquivo,
# # \n é só mais um carácter.
# # Felizmente, o Python sabe que estes são caracteres especiais e você pode pedir para ler uma linha por vez. Vamos experimentar!
#
#Le uma Linha do arquivo
with open('camelot.txt') as song:
    print(song.readline())

# Todo: Convenientemente, o Python executará um loop sobre as linhas do arquivo utilizando a sintaxe for line in file.
# Eu posso usar isso para criar uma lista de linhas no arquivo. Como cada linha ainda tem o seu caractere de nova linha anexado,
# eu removo-o usando .strip().

camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)