carrots = 24
rabbits = 8
crs_per_rab = carrots/rabbits
rabbits = 12
print(crs_per_rab)

sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

mais_densa = (san_francisco_pop_density > rio_de_janeiro_pop_density)

print(mais_densa)

if (san_francisco_pop_density > rio_de_janeiro_pop_density):
    print(True)
else:
    print(False)

one_name = 'Deyveson'
two_name = 'Willian'

name_complete = (one_name + ' ' + two_name)
print(name_complete)

name = len("Deyveson")
print(name)

# Quiz: Vendas totais
# Neste quiz, você precisará alterar os tipos dos dados de entrada e de saída a fim de obter o resultado desejado.
#
# Calcule e exiba o total de vendas da semana a partir dos dados fornecidos.
# Exiba uma string da forma "This week's total sales: xxx", onde xxx será o total real de todos os números.
# Você precisará alterar os tipos de dados de entrada a fim de calcular o total.

mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

total_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)

mensagem = 'This week\'s total sales:' + ' ' + str(total_sales)

print(mensagem)

print('DEYVESON'.isnumeric())

nome='deyveson'
sobrenome='willian'

new_str = "The cow jumped over the moon."
print(new_str.split(None, 3))