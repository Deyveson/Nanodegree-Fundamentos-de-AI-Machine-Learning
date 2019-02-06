#Todo: Quiz: Calcular um expoente
# É sua vez de importar e usar o módulo de math. Use o módulo math para calcular e elevado à potência 3. Use print para exibir a resposta.
# Veja a documentação do módulo de matemática para encontrar a função que você precisa!

import math
print(math.exp(3))

#Todo: Quiz: Gerador de senha
# Escreva uma função chamada generate_password que seleciona três palavras aleatórias de um arquivo de palavras fornecido
# e as concatena em uma única string. O código para ler os dados do arquivo já está no código inicial, você precisará construir
# uma senha a partir destas peças.

# Use uma declaração de importação no topo
import random;

word_file = "words.txt"
word_list = []

#vendo o que tem no arquivo
# f = open('words.txt', 'r')
# file_data = f.read()
# print(file_data)

# preencha a lista de palavras
with open(word_file,'r') as words:
	for line in words:
        # remova o espaço em branco e faça tudo em minúsculas
		word = line.strip().lower()
        # não inclua palavras muito longas ou muito curtas
		if 3 < len(word) < 8:
			word_list.append(word)

print(word_list)

# Adicione sua função generate_password aqui
# Deve devolver uma string composta por três palavras aleatórias
# concatenados juntos sem espaços

#Solução 1
# def generate_password():
#     return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)

# Solução 2
def generate_password():
    return ''.join(random.sample(word_list,3))

# test your function
print(generate_password())




