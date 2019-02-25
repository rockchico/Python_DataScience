my_tuple = (4, 5)

# não pode
# my_tuple[1] = 0

def sum_and_product(x, y):
    return (x + y), (x * y)

print(sum_and_product(3, 5))


x, y = 10, 43
x, y = sum_and_product(3, 5)

print(x)
print(y)