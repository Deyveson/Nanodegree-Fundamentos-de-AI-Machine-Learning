# Quiz: Qual é o prêmio
# A tabela abaixo apresenta qual é o prêmio que um concorrente de uma competição ganharia com uma determinada quantidade de pontos. Escreva uma declaração
# if que permite que um concorrente saiba qual destes prêmios ganhou, com base no número de pontos marcado (no código, representada pela variável de tipo inteiro points).
#
# Pontos	Prêmio
# 1 - 50	coelho de madeira
# 51 - 150	nenhum prêmio
# 151 - 180	hortelã wafer-fina
# 181 - 200	pinguim
# Todos os limites inferiores e superiores aqui são inclusivos, e points pode assumir apenas valores inteiros positivos até 200. Ou seja,
# não é necessário se preocupar com o resultado obtido para números fora das faixas apresentadas na tabela.
#
# Na sua declaraçãoif, atribua à variável result uma string contendo a mensagem apropriada com base no valor de points:
#
# Se eles ganharam um prêmio, deve exibir a mensagem "Congratulations! You won a [prize name]!", com o nome do prêmio.
# Caso o concorrente não ganhe nenhum prêmio (points na faixa 51-150), deve exibir a mensagem "Oh dear, no prize this time.".
# OBS: Ao enviar sua solução points deve ter valor 174 para que o quiz seja corrigido corretamente.

points = 174  # Use essa entrada para fazer a submissão
result = ''


# escreva a declaração do if
if points >= 1 and points <= 50:
    result = 'Congratulations! You won a wooden rabbit!'
elif points >= 51 and points <= 150:
    result = 'Oh dear, no prize this time.'
elif points >= 151 and points <= 180:
    result = 'Congratulations! You won a wafer-thin mint!'
elif points >= 181 and points <= 200:
    result = 'Congratulations! You won a penguin!'

print("Quantidade de Pontos: {}".format(points))
print(result)


