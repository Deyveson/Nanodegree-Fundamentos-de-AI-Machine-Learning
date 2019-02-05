# # def my_range(x):
# #     i = 0
# #     while i < x:
# #         yield i
# #         i += 1
# #
# # for n in my_range(4):
# #     print(n)
# #
#
# # Todo: Quiz Implementando my_enumerate
# # Escreva sua própria função de gerador que funciona como a função interna enumerate.
# #
# # Recorrendo à função assim:
# #
# # lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]
# #
# # for i, lesson in my_enumerate(lessons, 1):
# #     print("Lesson {}: {}".format(i, lesson))
#
#
# lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]
#
# def my_enumerate(iterable, start=0):
#     count = start
#     for element in iterable:
#         yield count, element
#         count += 1
#
# for i, lesson in my_enumerate(lessons, 1):
#     print("Lesson {}: {}".format(i, lesson))
#
# # Todo: Quiz Chunker
# # Se você tem um iterável que é grande demais para caber na memória por completo (ex. ao lidar com arquivos grandes),
# # ser capaz de pegar e utilizar apenas pedaços a cada vez pode ser muito valioso.
# #
# # Implemente uma função de gerador, chunker, que recebe um iterável e retorna um pedaço de tamanho específico por vez.
#
#
# def chunker(iterable, size):
#     """Produza pedaços sucessivos de tamanho de tamanho iterável."""
#     for i in range(0, len(iterable), size):
#         yield iterable[i:i + size]
#
# for chunk in chunker(range(25), 4):
#     print(list(chunk))

# -----------------------------------------------------------------------

sq_list = [x**2 for x in range(10)]  # isto produz uma lista de quadrados

sq_iterator = (x**2 for x in range(10))  # isto produz um iterador de quadrados

for sq in len(sq_iterator():
    print(list(sq))