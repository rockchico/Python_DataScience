list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list3 = zip(list1, list2) # is [('a', 1), ('b', 2), ('c', 3)]

print(list(list3))



lista4 = [('a', 1), ('b', 2), ('c', 3)]

letras, numeros = zip(*lista4)

print(letras)
print(numeros)


def add(a, b):
    return a + b

add(1, 2)
add([1, 2])
add(*[1, 2])