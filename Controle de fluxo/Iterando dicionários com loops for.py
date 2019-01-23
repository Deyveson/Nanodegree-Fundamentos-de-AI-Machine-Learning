# Todo: Quando você iterar um dicionário usando um loop for,
# fazer do jeito normal (for n in some_dict) vai apenas dar acesso às chaves do dicionário - que é o que queremos em algumas situações.
# Em outros casos, queremos iterar as _chaves_e_valores_ do dicionário. Vamos ver como isso é feito a partir de um exemplo.
# Considere este dicionário que usa nomes de atores como chaves e seus personagens como valores.

cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

print("Iterando pelas chaves:")
for key in cast:
    print(key)

print("\nIterando pelas chaves e valores:")
for key, value in cast.items():
    print("Ator: {}    Papel: {}".format(key, value))
