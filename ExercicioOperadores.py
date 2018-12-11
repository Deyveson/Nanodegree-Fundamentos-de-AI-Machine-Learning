# Escreva uma expressao que calcule a media de 23, 32 e 64
# Ou seja, some os tres numeros e divida por 3.0
# Coloque a expressao dentro do print
print((23 + 32 + 64)/3.0)


# Neste quiz, você vai fazer alguns cálculos para um ladrilhador. Duas partes de um piso precisam de azulejos.
# Uma parte tem 9 azulejos de largura por 7 azulejos de comprimento, a outra tem 5 azulejos de largura por 7 azulejos de comprimento. Os azulejos vêm em pacotes de 6.
# Quantos azulejos são necessários?
# Você compra 17 pacotes, contendo 6 azulejos em cada. Quantos azulejos vão sobrar?

# Preencha com uma expressão que calcule quantos azulejos são necessários.
lado1 = (9*7)
lado2 = (5*7)
totalazulejos = (lado1 + lado2)
print(totalazulejos)
# Preencha com uma expressão que calcule quantos azulejos sobrarão.
azulejos = 17 * 6
sobra = azulejos - totalazulejos
print(sobra)


print (((3 + 32)) + -15//2)
print((3 + 32) + -15//2)

print ((17 - 6) % (5 + 2))

print ((1 + 2 + 4) / 13)
print((1 + 2 + 4)/13)

print (4/2 - 7*7)

print((23 + 32 + 64)/3.0)

# Volume atual de um reservatório de água (em metros cúbicos)
reservoir_volume = 4.445 * 10 ** 8

# Total de água da chuva de uma tempestade(em metros cúbicos)
rainfall = 5 * 10 ** 6

# Reduza a variável de água da chuva(rainfall) em 10% para considerar perdas
rainfall -= rainfall * 0.1

# Adicione a variável rainfall à variaável de vol. atual do reservatório(reservoir_volume)
reservoir_volume += rainfall

# aumente o volume do reservatório (reservoir_volume) em 5% para considerar águas tempestuosas
# que chegam no reservatório dias apoós a tempestade
reservoir_volume += reservoir_volume * 0.05
print(reservoir_volume)

# reduza o volume do reservatório (reservoir_volume) em 5% para considerar evaporaçaão
reservoir_volume -= reservoir_volume * 0.05
print(reservoir_volume)

# Subtraia 2.5e5 metros cúbicos de reservoir_volume para considerar água
# que édirecionada para regiões áridas.
metros_cubicos = 2.5 * 10 ** 5
reservoir_volume -= metros_cubicos

#execute um print do novo valor de reservoir_volume
print(reservoir_volume)

