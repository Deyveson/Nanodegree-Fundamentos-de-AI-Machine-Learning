# Todo: Quiz - Usando range, interando no array e exibindo maiúsculo .title()

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

print(cities)

for index in range(len(cities)):
    cities[index] = cities[index].title()
    print(cities[index])


# Todo: Quiz - Criando o nome de usuários
# Escreva um loop for que itere sobre a lista names para criar uma lista usernames. Para criar um nome de usuário para cada nome, faça tudo em letras minúsculas e substitua os espaços por sublinhados. Executando seu loop for sobre a lista:
#
# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
#
# deve criar a lista:
#
# usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]


names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing",
         "Phoebe Buffay"]
usernames = []

for name in names:
    usernames.append(name.lower().replace(" ", "_"));

print(usernames)


# Todo: Quiz - Modificando o nome de usuários com range
# Escreva um loop que usa range() para iterar sobre as posições em usernames e modificar a lista.
# Como você fez no quiz anterior, altere cada nome para que tenha letras minúsculas e substitua os espaços por sublinhados. Depois de executar seu loop, esta lista
#
# usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
#
# deve mudar para isto:
#
# usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]


usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for index in range(len(usernames)):
    usernames[index] = (usernames[index].lower().replace(" ", "_"));

print(usernames)


# Todo: Quiz - Contador de tags
# Escrever um loop for que itere sobre uma lista de strings e tokens e conte quantos deles existem tags XML.
# XML é uma linguagem de dados semelhante ao HTML. Você pode dizer que uma string é uma tag XML se ela começar com
# um colchete angular esquerdo "<" e acabar com um colchete angular direito ">". Monitore o número de tags utilizando a variável count.
#
# Você pode assumir que a lista de strings não vai conter strings vazias.


tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here

for token in tokens:
    count += token.count('<')

print(count)

# Todo: Quiz - Criando uma lista HTML
# Escreva um loop for que itere sobre uma lista de strings e crie uma única string, html_str, que é uma lista HTML. Por exemplo,
# se a lista for items = ['first string', 'second string'], a saída exibida para html_str deve ser:
#
# <ul>
# <li>first string</li>
# <li>second string</li>
# </ul>
# Ou seja, a primeira linha da string deve ser a tag de abertura <ul>. Depois disso, vem uma linha para cada elemento na lista fonte,
# cercado por tags <li> e </li>. A última linha da string deve ser a tag de fechamento </ul>.

items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here

for index in range(len(items)):
   html_str += ("\n<li>" + items[index] + "</li> \n")
html_str += "\n</ul>"
print(html_str)

#Todo: Se você quisesse criar uma nova lista chamada lower_colors, em que cada cor em colors estivesse em letras minúsculas, que código faria isso?

colors = ['Red', 'Blue', 'Green', 'Purple']
lower_colors = [ ]

for color in colors:
    lower_colors.append(color.lower())

print(lower_colors)

# Todo: Exemplos usando range
print(list(range(4)))

print(list(range(4,8)))

print(list(range(4,10,2)))

print(list(range(0,-5)))