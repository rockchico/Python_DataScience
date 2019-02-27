from functools import reduce
import math
from collections import Counter
from matplotlib import pyplot as plt

# this isn't right if you don't from __future__ import division
def mean(x):
    return sum(x) / len(x)
    

def median(v):
    """finds the 'middle-most' value of v"""
    n = len(v)
    sorted_v = sorted(v)
    #print(sorted_v)

    midpoint = n // 2
    if n % 2 == 1:
        # if odd, return the middle value
        return sorted_v[midpoint]
    else:
        # if even, return the average of the middle values
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2


def quantile(x, p):
    """returns the pth-percentile value in x"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]

def mode(x):
    """returns a list, might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
        if count == max_count]

def data_range(x):
    return max(x) - min(x)

def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


def sum_of_squares(v):
    """computes the sum of squared elements in v"""
    return sum(v_i ** 2 for v_i in v)

def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

def standard_deviation(x):
    return math.sqrt(variance(x))


def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i
        for v_i, w_i in zip(v, w))


def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0 # if no variation, correlation is zero
    


def make_friend_counts_scatterplots(friends, minutes, labels):
    plt.scatter(friends, minutes)
    # label each point
    for label, friend_count, minute_count in zip(labels, friends, minutes):
        plt.annotate(label,
            xy=(friend_count, minute_count), # put the label with its point
            xytext=(5, -5), # but slightly offset
            textcoords='offset points'
        )
    plt.title("Daily Minutes vs. Number of Friends")
    plt.xlabel("# of friends")
    plt.ylabel("daily minutes spent on the site")
    plt.show()


""" ****************************************************************************** """


num_friends =   [2      ,4,     7,      8,      3,      8,      9,      10,     20]
daily_minutes = [100    , 45,   80,     200,    400,    300,    100,    90,     150]
labels =        ['a'    ,'b'    ,'c'    ,'d'    ,'e'    ,'f'    ,'g'    ,'h'    ,'i']

#num_friends = [10, 10, 10, 10]
print("mediana = ",median(num_friends)) 
print("media = ",mean(num_friends))



print(quantile(num_friends, 0.10))
print(quantile(num_friends, 0.20))
print(quantile(num_friends, 0.25))
print(quantile(num_friends, 0.75))
print(quantile(num_friends, 0.90))


print("moda = ", mode(num_friends))
print("data range ", data_range(num_friends))
print("variancia", variance(num_friends))
print("standardt deviation = ", standard_deviation(num_friends))
print("covariancia = ", covariance(num_friends, daily_minutes))
print("correlation = ", correlation(num_friends, daily_minutes))


# make_friend_counts_histogram()

make_friend_counts_scatterplots(num_friends, daily_minutes, labels)