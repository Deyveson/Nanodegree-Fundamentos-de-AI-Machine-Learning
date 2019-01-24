# letters = ['a', 'b', 'c']
#
# nums = [1, 2, 3]
#
# resul = []
#
# for letter, num in zip(letters, nums):
#     resul += ("{}: {}".format(letter, num)),
#
# print(resul)


# resul = [('a', 1), ('b', 2), ('c', 3)]
# letters, nums = zip(*resul)
#
# print(letters)
# print(nums)


# letters = ['a', 'b', 'c', 'd', 'e']
# for i, letter in enumerate(letters):
#     print(i, letter)

# todo: Quiz Coordenadas zip
# Use zip para gravar um loop for que cria uma string especificando o rótulo e as coordenadas de cada ponto e acrescenta à lista points.
# Cada string deve ser formatada como label: x, y, z. Por exemplo, a string para a primeira coordenada deve ser F: 23, 677, 4.
#
# x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
# y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
# z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
# labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]
#
# points = []
# # write your for loop here
#
# for label, x, y, z in zip(labels, x_coord, y_coord, z_coord):
#     points += ("{}: {}, {}, {}".format(label, x, y, z)),
# print(points)

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []

for label, x, y, z in zip(labels, x_coord, y_coord, z_coord):
    points += ("{}: {}, {}, {}".format(label, x, y, z)),

print(points)


