import	re	as	regex

def double(x):
    """ opa """
    return x * 2


def aply_to_one(f):
    """ chama a função f passando parametro 1 """
    return f(1)


my_double = double
x = aply_to_one(my_double)

y = aply_to_one(lambda x: x + 4)

print(x)
print(y)
