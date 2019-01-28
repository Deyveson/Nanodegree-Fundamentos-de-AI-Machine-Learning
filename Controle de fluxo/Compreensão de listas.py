# #Exemplo 1 Compreensão de listas
#
# cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
#
# capitalized_cities = []
#
# for city in cities:
#     capitalized_cities.append(city.title())
#
# print(capitalized_cities)
#
# #Exemplo 1 com Compreenção de listas
#
# capitalized_cities = [city.title() for city in cities]
#
# print(capitalized_cities)
#
# #Exemplo lista de numeros quadrados
#
# squares = []
#
# for x in range(9):
#     squares.append(x**2)
# print(squares)
#
# #Exemplo com List Comprehension
# squares = [x**2 for x in range(9)]
#
# print(squares)
#
# #adcionando uma condição a List Comprehension
# squares = [x**2 for x in range(9) if x % 2 ==0]
# print(squares)
#
# #Para adicionar um else
#
# squares = [x**2 if x % 2 ==0 else x + 3 for x in range(9)]
# print(squares)
#
# # Todo: Quiz Extraindo os primeiros nomes
# # Use uma compreensão de listas para criar uma nova lista first_names,
# # que contém apenas os primeiros nomes em names em letras minúsculas.
#
#
# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
#
# first_names = [] # write your list comprehension here
#
# first_names = [name[:5].replace(' ', '').lower() for name in names]
#
# print(first_names)
#
#
# # Todo: Quiz: Múltiplos de três
# # Use uma compreensão de listas para criar uma lista multiples_3, contendo os 20 primeiros múltiplos de 3.
#
# multiples_3 = []
# multiples_3 = list([x**1 for x in range(60) if x % 3==0])
#
# print(multiples_3)



# Todo: Quiz Filtro de nomes por pontuações
#Use uma compreensão de lista para criar uma lista de nomes passed, que só incluem aqueles que marcaram pelo menos 65 pontos.


scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }
#
# passed = [scores for key in scores if scores.values() >= 65]

# passed = []
#

passed = scores.values();

print(passed)
