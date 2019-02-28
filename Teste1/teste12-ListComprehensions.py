even_numbers = [x for x in range(10) if x % 2 == 0]

print(even_numbers)

squares = [x * x for x in range(5)]

print(squares)

even_squares = [x * x for x in even_numbers]

print(even_squares)

square_dict	= {	x: x * x for x in range(5) }		#	{	0:0,	1:1,	2:4,	3:9,	4:16	}
square_set = { x + x for x in [2, -2] }	#	{	1	}

print(square_dict)
print(square_set)

zeroes = [0	for	_ in even_numbers] #	has	the	same	length	as	even_numbers

print(zeroes)

pairs =	[(x, y)
			for	x	in	range(3)
			for	y	in	range(3)]			#	100	pairs	(0,0)	(0,1)	...	(9,8),	(9,9)

print(pairs)

pairs =	[(x, y)
			for	x	in	range(3)
			for	y	in	range(x+1, 3)]			#	100	pairs	(0,0)	(0,1)	...	(9,8),	(9,9)

print(pairs)