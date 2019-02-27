from functools import reduce
import math

def vector_add(v, w):
    """adds corresponding elements"""
    return [v_i + w_i for v_i, w_i in zip(v, w)]

def vector_subtract(v, w):
    """adds corresponding elements"""
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def scalar_multiply(c, v):
    """c is a number, v is a vector"""
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    """compute the vector whose ith element is the mean of the
    ith elements of the input vectors"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def vector_sum(vectors):
    """sums all corresponding elements"""
    result = vectors[0] # start with the first vector
    for vector in vectors[1:]: # then loop over the others
        result = vector_add(result, vector) # and add them to the result
    return result

def vector_sum2(vectors):
    return reduce(vector_add, vectors)


def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i
        for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)



def magnitude(v):
    return math.sqrt(sum_of_squares(v)) # math.sqrt is square root function


def squared_distance(v, w):
    """(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
    return magnitude(vector_subtract(v, w))



""" ***************************************************************** """

x = [6, 3, 1]
y = [8, 5, 4]
z = [0, 1, 2]

print(vector_sum([x, y, z]))
print(vector_sum2([x, y, z]))
print(vector_mean([x, y, z]))
print(dot(x, y))

print(distance(x, y))


"""
x = ['ggg', 'hhh', 'ppp']
y = [8, 5, 4]
z = ["@", "%", "&"]


r1 = zip(x, y, z)
print(list(r1))
"""