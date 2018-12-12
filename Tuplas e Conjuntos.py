
lista = "\n".join(["deyveson", "willian", "gomes", "rodrigues"])
print(lista)

print("\n")
lista1 = ["deyveson", "willian", "gomes", "rodrigues"]
print("-".join(lista1))

lista1.append('dogmal')
print(lista1)

a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))

names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))

names = ["Carol", "Albert", "Ben", "Donna"]
names.append("Eugenia")
print(sorted(names))

numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums)

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
b.add(5)
b.pop()

print(b)