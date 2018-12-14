# Quiz: Usando valores verdade de objetos
# Reescreva seu código do quiz anterior. Qual é o prêmio, usando o que aprendeu sobre valores verdade. Comece definindo a variável prize para None e,
# em seguida, use uma declaração if para reatribuir o nome apropriado do prêmio ao 'Prêmio', caso eles tenham ganhado um prêmio. Depois disso,
# use outra declaração if para atribuir result à string correta baseada no valor verdade de prize. Assim, não teremos múltiplas atribuições de resultado.


points = 174

premio = None


if points <= 50:
    premio = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    premio = "Oh dear, no prize this time."
elif points <= 180:
    premio = "Congratulations! You won a wafer-thin mint!"
else:
    premio = "Congratulations! You won a penguin!"

if(premio!=False):
    result=premio

print(result)


#Solução do Quiz da Udacity

points = 174
prize = None

if points <= 50:
    prize = "a wooden rabbit"
elif 151 <= points <= 180:
    prize = "a wafer-thin mint"
elif points >= 181:
    prize = "a penguin"

if prize:
    result = "Congratulations! You won " + prize + "!"
else:
    result = "Oh dear, no prize this time."

print(result)