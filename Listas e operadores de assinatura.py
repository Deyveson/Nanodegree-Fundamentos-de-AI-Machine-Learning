# Você está in OU not in?
# Você viu que nós também podemos usar in e not in para retornar um bool
# que afirma se um elemento existe ou não dentro de nossa lista ou se uma string é uma substring de outra.

hello = 'Hello There'

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

print('Sunday' in months, 'Sunday' not in months)


# Use a indexação de lista para determinar quantos dias existem em um mês específico com base na variável month, de tipo inteiro,
# e armazene esse valor na variável de tipo inteiro num_days. Por exemplo, se month for 8,
# num_days deve ser definida como 31, já que o oitavo mês, agosto, possui 31 dias.
#
# Lembre-se de considerar que a indexação é baseada no zero!


month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]


num_days = days_in_month[month]

print(num_days)


# Quiz: Cortando listas
# Selecione as três datas mais recentes desta lista usando a notação de corte de lista.
# Dica: índices negativos funcionam para as fatias!


eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']

print(eclipse_dates[-3:])


sentence1 = "I wish to register a complaint."
sentence2 = ["I", "wish", "to", "register", "a", "complaint", "."]

sentence2[6]="!"

print(sentence2)

sentence2[0]= "Our Majesty"

print(sentence2)




sentence2[0:2] = ["We", "want"]

print(sentence2)

