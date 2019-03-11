x = 0

while x < 10:
    print(x, "é menor que 10")
    x += 1



for x in range(10):
    print(x, "é menor que 10 .... for in")


for	x	in	range(10):
    if	x	==	3:
        continue		#	go	immediately	to	the	next	iteration
    if	x	==	5:
        break					#	quit	the	loop	entirely
    print(x)