# Todo: Compactando
letters = ['a', 'b', 'c']

nums = [1, 2, 3]

resul = []

for letter, num in zip(letters, nums):
    resul += ("{}: {}".format(letter, num)),

print(resul)

# Todo: Descompactando
resul = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*resul)

print(letters)
print(nums)

# Todo: Exemplo Enumerate
letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)

# todo: Quiz Coordenadas zip
# Use zip para gravar um loop for que cria uma string especificando o rótulo e as coordenadas de cada ponto e acrescenta à lista points.
# Cada string deve ser formatada como label: x, y, z. Por exemplo, a string para a primeira coordenada deve ser F: 23, 677, 4.

#Minha Solução
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here

for label, x, y, z in zip(labels, x_coord, y_coord, z_coord):
    points += ("{}: {}, {}, {}".format(label, x, y, z)),
print(points)

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]


points = []

for label, x, y, z in zip(labels, x_coord, y_coord, z_coord):
    points += ("{}: {}, {}, {}".format(label, x, y, z)),

print(points)

#Solução Udacity

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point))

for point in points:
    print(point)

# Todo: Quiz: Listas zip para dicionário
# Use zip para criar um dicionário cast que usa names como chave e heights como valores.

#Minha Solução
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = []
# replace with your code

cast = (list(zip(cast_names, cast_heights)))

print(cast)

#Solução Udacity
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))
print(cast)

# Todo: Quiz: Enumerate
# Use enumerate para modificar a lista cast para que cada elemento contenha o nome seguido da altura correspondente do personagem.
# Por exemplo, o primeiro elemento de cast deve mudar de "Barney Stinson" para "Barney Stinson 72".

#Minha Solução
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# write your for loop here
cat = []

for i, casts in enumerate(cast):
    cat += "{} {}".format(casts, heights[i]),

cast = cat;

print(cast)


#Solução Udacity
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

for i, character in enumerate(cast):
    cast[i] = character + " " + str(heights[i])

print(cast)

# Todo: Quiz Tuplas descompactadas

#Minha Solução

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

names, heights = zip(*cast)

print(names)
print(heights)

# Todo Quiz: Transposição com zip
# Use zip para transpor data de uma matriz 4 por 3 para uma matriz 3 por 4. Na verdade, existe um truque legal para isso!
# Fique à vontade para olhar para as soluções, caso não consiga descobrir.

#Solução
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)