# Experimente trabalhar com dicionários aninhados. Adicione uma outra entrada, 'is_noble_gas',
# para cada dicionário no dicionário elements.
# Depois de inserir as novas entradas, você deve ser capaz de executar estas pesquisas:
#
# todo: Adicione uma entrada 'is_noble_gas' para hydrogen e helium identificando se são gases nobres
# dica: helium é um gás nobre, hydrogênio não


elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True

print(elements)

print(elements['hydrogen']['is_noble_gas'])

print(elements['helium']['is_noble_gas'])


# Quiz: Conte palavras únicas
# Sua tarefa para este quiz é encontrar o número de palavras únicas no texto. No editor de código abaixo, complete estes três passos para obter sua resposta.
#
# Separe verse em uma lista de palavras.
# Converta a lista para uma estrutura de dados capaz de armazenar apenas seus elementos únicos.
# Exiba o comprimento do container escolhido no item 2.
# Dica: Você pode usar um método de string visto nos tópicos anteriores.

verse = "if you can keep your head when all about you are losing theirs and blaming it on you   " \
        "if you can trust yourself when all men doubt you     but make allowance for their doubting too   " \
        "if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   " \
        "or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"

print(verse, '\n')

# dividir o verso na lista de palavras
verse_list = verse.split()
print(verse_list, '\n')

# converter lista para uma estrutura de dados que armazena elementos unicosl
verse_set = set(verse_list)
print(verse_set, '\n')

# imprimi o número de palavras unicas
num_unique = len(verse_set)
print(num_unique, '\n')

verse_dict = {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

# encontre o número de chaves únicas no dicionário
num_keys = len(verse_dict)
print(num_keys)

#-----------------------------------------------
#Procurando se 'breathe' tem na lista 1º maneira
contains_breathe = verse_dict.get('breathe')
print(contains_breathe)
#Procurando se 'breathe' tem na lista 2º maneira
contains_breathe = "breathe" in verse_dict
print(contains_breathe)
#-----------------------------------------------


# crie e ordene uma lista das chaves do dicionário

sorted_keys = sorted(verse_dict.keys())

sorted_keys = verse_dict.keys()
print(sorted_keys)

sorted_keys = sorted(sorted_keys)
print(sorted_keys)


# Exibe o ultimo valor da lista
print(sorted_keys[-1])
# Exibe o primeiro valor da lista
print(sorted_keys[0])
#Exibe o maior valor da lista
print(max(sorted_keys))
















