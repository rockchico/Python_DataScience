integer_list = [4,6,8]
hetero_list = ["string", 0.1, 1, True]


list_of_lists = [integer_list, hetero_list, "opa"]

list_length = len(integer_list)
list_sum = sum(integer_list)

print(list_length)
print(list_sum)


x =	list(range(10))
first_three	= x[:3]															#	[-1,	1,	2]
three_to_end = x[3:]																#	[3,	4,	...,	9]
one_to_four	= x[1:5]																#	[1,	2,	3,	4]
last_three = x[-3:]																	#	[7,	8,	9]
without_first_and_last = x[1:-1]				#	[1,	2,	...,	8]
copy_of_x = x[:]																				#	[-1,	1,	2,	...,	9]

print(x)
print(first_three)
print(three_to_end)
print(one_to_four)
print(last_three)
print(without_first_and_last)
print(copy_of_x)

x.extend([66,88,44])
print(x)

x = x + [43,65,76]
print(x)

print(1 in x)

x, y = [1, 2] 
print('x')
print(x)
print('y')
print(y)

