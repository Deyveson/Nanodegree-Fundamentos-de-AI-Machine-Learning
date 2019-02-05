# Quiz: Lista do elenco de Flying Circus
# Você vai criar uma lista dos atores que apareceram no programa de televisão Flying Circus do Monty Python.
#
# Escreva uma função chamada create_cast_list, que recebe um nome de arquivo como entrada e retorna uma lista com o nome dos atores.
# Ela será executado sobre o arquivo flying_circus_cast.txt (essa informação foi recolhida de imdb.com).
# Cada linha do arquivo consiste no nome do ator, uma vírgula e algumas informações (desarrumadas) sobre os papéis em que eles atuaram no programa.
# Você precisará extrair apenas o nome e adicioná-lo a uma lista. Você pode usar o método .split() para processar cada linha.
#


#Minha Solução 1
# cast_list = []
# with open("flying_circus_cast.txt") as f:
#     for line in f:
#         cast_list.append(line.split(',')[0])
#
# print(cast_list)

#Minha solução 2
def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
        for line in f:
            name = line.split(',')[0]
            cast_list.append(name)
    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)


#Solução Udacity
# def create_cast_list(filename):
#     cast_list = []
#     with open(filename) as f:
#         for line in f:
#             name = line.split(",")[0]
#             cast_list.append(name)
#
#     return cast_list
#
# cast_list = create_cast_list('flying_circus_cast.txt')
# for actor in cast_list:
#     print(actor)
