elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
n = elements.get("dilithium")
print(n is None)
print(n is not None)


print("carbon" in elements)
print(elements.get("dilithium"))


population = {17.8: "Shanghai", 13.3: "Istanbul", 13.0: "Karachi", 12.5: "Mumbai"}
print(population)



a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)

animals = {'dogs': [20, 10, 15, 8, 32, 15], 'cats': [3,4,2,8,2,4], 'rabbits': [2, 3, 3], 'fish': [0.3, 0.5, 0.8, 0.3, 1]}

print(animals['fish'])