# exemplo:
double = lambda x: x * 2
print(double(3))

# Função comun
def multiply(x, y):
    return x * y

# Função lambda
multiply = lambda x, y: x * y

print(multiply(3, 2))

# Nao resolvi
lambda x, y: x * y


# Todo : Quiz Lambda com mapa
# map() é uma função interna de ordem superior que aceita uma função e um iterável como entradas e devolve
# um iterador que aplica a função para cada elemento do iterável. O código abaixo usa map() para encontrar a média de cada
# lista em numbers e criar a lista averages. Teste para ver o que acontece.
#
# Reescreva esse código para ser mais conciso, substituindo a função mean por uma expressão lambda definida dentro
# da chamada de map().
#
# Em outras palavras: map recebe qualquer função como primeiro parâmetro e uma lista como segundo parâmetro,
# nesse exemplo a função mean e a lista numbers, e aplica a função a todos elementos da lista, um a um. O resultado obtido é um objeto do tipo map com as médias de cada lista em numbers. Na linha 11, o retorno da função é convertido de volta para list.

numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

# Solução normal
# def mean(num_list):
#     return sum(num_list) / len(num_list)
#
# averages = list(map(mean, numbers))

#  ------------------------------------------------------------

# Solução com Lambda
mean = lambda num: sum(num) / len(num)
# 'mean' nome da função, 'lambda' pra dizer que e uma função ocuta,
# 'num' o parametro da funcao
# 'sum(num)' soma os valores da linha da função
# 'len(num)' soma a quantidade de itens por linha

averages = list(map(mean, numbers))
# map recebe qualquer função como primeiro parâmetro e uma lista como segundo parâmetro

print(averages)


# Todo: Quiz Lambda com filtro
# filter() é uma função interna de ordem superior que aceita uma função e um iterável como entradas e
# devolve um iterador com os elementos do iterável para os quais a função retorna o valor true. O código abaixo usa filter()
# para obter os nomes em cities que possuem menos de 10 caracteres de tamanho para criar a lista short_cities.
# Execute um teste para ver o que acontece.
#
# Reescreva esse código para ser mais conciso, substituindo a função is_short por uma expressão lambda definida
# dentro da chamada de filter().


# Solução Udacity

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

# Exemplo para aplicar lambda
# def is_short(name):
#     return len(name) < 10
#
# short_cities = list(filter(is_short, cities))

#Minha solução do codigo acima
is_short = lambda name: len(name) < 10
short_cities = list(filter(is_short, cities))

# Solução Udacity
short_cities = list(filter(lambda x: len(x) < 10, cities))

print(short_cities)



