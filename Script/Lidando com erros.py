
#Se o valor nao for int ele retorna a mensagem 'except'

while True:
    try:
        x = int(input('Digite um numero: '))
        print('Numero digitado {}'.format(x))
        break
    except:
        print('Esse numero não e valido')
    finally:
        print('\n Attempted Input \n')



#Posso tratar o tipo de 'ValueError', lançando a mensagem especifica
while True:
    try:
        x = int(input('Digite um numero: '))
        print('Entrada Valida: {}'.format(x))
        break
    except ValueError:
        print('\nEssa entrada não e valida\n')
    except KeyboardInterrupt:
        print('\nSem tentativa de entrada\n')
        break
    finally:
        print('\n Attempted Input \n')