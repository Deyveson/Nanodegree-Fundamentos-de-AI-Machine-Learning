# Todo: Criando dicionários
# Você já está familiarizado com dois importantes conceitos: 1) contagem usando loops for e 2)
# o método get dos dicionários. Na verdade, ambos os conceitos podem ser combinados para criar um contradicionário bastante útil,
# com o qual é provável que você se depare novamente. Por exemplo, podemos criar um dicionário,
# word_counter, que controla o número total de cada palavra em uma string.

book_title = ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']

word_counter = {}

# #Primeira mandeira de fazer
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1

# Segunda maneira de fazer

for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1

print(word_counter)















