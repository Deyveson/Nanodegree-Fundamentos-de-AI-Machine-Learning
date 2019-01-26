#Exemplo 1 Compreensão de listas

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())

print(capitalized_cities)

#Exemplo 1 com Compreenção de listas

capitalized_cities = [city.title() for city in cities]

print(capitalized_cities)

#Exemplo lista de numeros quadrados

squares = []

for x in range(9):
    squares.append(x**2)
print(squares)

#Exemplo com List Comprehension
squares = [x**2 for x in range(9)]

print(squares)

#adcionando uma condição a List Comprehension
squares = [x**2 for x in range(9) if x % 2 ==0]
print(squares)

#Para adicionar um else

squares = [x**2 if x % 2 ==0 else x + 3 for x in range(9)]
print(squares)