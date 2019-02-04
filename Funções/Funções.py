
# Todo: Quiz Função de densidade populacional
# Escreva uma função chamada population_density que aceita dois argumentos, population e land_area,
# e devolve uma densidade populacional calculada a partir desses valores.
# Eu incluí dois casos de teste que você pode usar para verificar se sua função funciona corretamente.
# Uma vez que você já escreveu sua função, use o botão de execução de teste para testar seu código.


# write your function here
def population_density(population, land_area):
    return population / land_area;

# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))


# Todo : Quiz readable_timedelta
# Escreva uma função chamada readable_timedelta que receba um argumento, um número inteiro days,
# e devolva uma string que diz quantas semanas e dias esse número representa.
# Por exemplo, readable_timedelta(10) deve devolver, "1 week(s) and 3 day(s)."

def readable_timedelta(days):
    # use integer division to get the number of weeks
    weeks = days // 7
    # use % to get the number of days that remain
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)

print(readable_timedelta(8))