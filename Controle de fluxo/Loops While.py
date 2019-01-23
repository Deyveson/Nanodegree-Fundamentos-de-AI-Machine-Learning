card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

# adiciona o último elemento da lista card_deck à lista hand
# até que os valores na mão somam 17 ou mais

while sum(hand) <= 17:
    hand.append(card_deck.pop())

print(hand)


# todo: Quiz Quadrado mais próximo
# Escreva um loop while que encontra o maior número quadrado que seja menor que um inteiro limit e armazena-o na variável nearest_square.
# Um número quadrado é o produto de um número inteiro multiplicado por si mesmo, por exemplo, 36 é um número quadrado, porque é igual a 6*6.
#
# Por exemplo, se limit for 40, seu código deve definir o nearest_square para 36.

# Meu Exemplo
limit = 40
ctl = 1;

while ctl <= 10:
   nearest_square = ctl ** 2
   if(nearest_square == 36):
       break;
   ctl += 1;

print(nearest_square)

#Exemplo Udacity
limit = 40
num = 0

while (num+1)**2 < limit:
    num += 1
nearest_square = num**2

print(nearest_square)