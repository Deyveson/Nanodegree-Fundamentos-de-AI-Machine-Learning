# f = open('test.txt', 'r')
#
# file_data = f.read()
# f.close()
#
# print(file_data)
#
# file = []
# for i in range(100000):
#     file.append(open('test.txt', 'r'))
#     print(i)


# 1 - Cria um arquivo e grava
f = open('another_file.txt', 'w')
f.write('Hello World !')
f.close()


# 2 - depois ler
f = open('another_file.txt', 'r')
file_data = f.read()
f.close()

print(file_data)


#Desse moto ele abre o arquivo, le e fecha automatico
# with open('another_file.txt', 'r') as f:
#     file_data = f.read()
# print(file_data)