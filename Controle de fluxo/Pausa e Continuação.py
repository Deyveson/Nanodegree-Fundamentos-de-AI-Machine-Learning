# Todo: Quiz Quebrando uma string
# Escreva um loop com uma declaração break para criar uma string, news_ticker, que tenha exatamente 140 caracteres de tamanho.
# Você deve criar o ticker de notícias adicionando manchetes da lista headlines, inserindo um espaço entre cada uma. Se necessário,
# você pode truncar a última manchete no meio, para que news_ticker tenha exatamente 140 caracteres de tamanho.
#
# Lembre-se de que a break funciona tanto para loops while como para for. Use o loop que parecer mais apropriado.
# Considere adicionar declarações print a seu código para ajudá-lo a resolver bugs.


# Minha Solução
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ''

for i in headlines:
    news_ticker += i + ' '

news_ticker = news_ticker[:140]
print(news_ticker)


#Solução Udacity
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)








