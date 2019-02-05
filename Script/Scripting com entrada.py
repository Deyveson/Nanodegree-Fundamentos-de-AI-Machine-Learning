# name = input("Enter your name: ")
# print("Hello there, {}!".format(name.title()))


#Encapsulando a entrada de dados
num = float(input('Enter a Number: '))
num += 20
print(num)

#Recebo um numero, e escrevo a string quantas vezes tiver no 'num'
num = int(float(input('Enter an integer: ')))
print('hello \n' * num)

# 'eval' avalia a expression, retorna o calculo dos valaores
x = eval(input('Enter an expression: '))
print(x)

#Outro exemplo com 'eval'
num = 30
x = eval('num + 42')
print(x)