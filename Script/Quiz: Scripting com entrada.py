# Todo: Quiz Gerando mensagens
# Imagine que você é um professor que precisa enviar uma mensagem a todos os alunos, lembrando-os das tarefas perdidas e atribuindo suas notas.
# Você possui todos os nomes, número de tarefas faltantes e as notas em uma planilha e só deve inserir esses dados nos espaços reservados nesta
# mensagem que você criou:
#
# Hi [inserir nome do aluno],
#
# This is a reminder that you have [inserir número de tarefas perdidas] assignments left to submit before you can graduate.
# Your current grade is [inserir nota atual] and can increase to [inserir nota potencial] if you submit all assignments before the due date.
#
# Você pode apenas copiar e colar esta mensagem para cada aluno e inserir manualmente os valores apropriados em cada vez, mas, em vez disso,
# vai escrever um programa que faz isso por você.
#
# Escreva um script que faz o seguinte:
#
# Pede 3 vezes uma entrada do usuário. Uma para obter uma lista de nomes, outra para obter uma lista de tarefas perdidas e uma última vez
# para obter uma lista de notas. Utilize esta entrada para criar as listas names, assignments e grades.
# Use um loop para exibir a mensagem para cada aluno com os valores corretos. A nota potencial é simplesmente a nota atual somada ao
# dobro do número de atividades perdidas.


names = input("Digite os nomes separados por vírgulas: ").title().split(",")
assignments = input("Insira as contagens de atribuição separadas por vírgulas: ").split(",")
grades = input("Insira notas separadas por vírgulas: ").split(",")


# string de mensagem a ser usada para cada aluno
# DICA: use .format() com esta string no seu loop for
# escreva um loop for que realize uma iteração em cada conjunto de nomes, tarefas e notas para imprimir a mensagem de cada aluno

message = "\n Oi {},\n\n Esse é um lembrete de que você tem {} atribuições deixadas para enviar antes que você possa se formar. " \
          "Sua nota atual é {} e pode aumentar para {} se você enviar todas as tarefas antes da data de vencimento.\n"


for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))

