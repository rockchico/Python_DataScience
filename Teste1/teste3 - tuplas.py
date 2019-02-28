my_list = [3, 4, 7]
my_tuple = (5,7,8)
other_tuple = 9, 8

try:
    my_tuple[0] = 4
except TypeError:
    print("não pode modificar tupla")


def sum_and_product(x, y):
    return (x + y), (x * y)

sp = sum_and_product(2, 3)
print(sp)
s, p = sum_and_product(2, 3)
print(s)
print(p)