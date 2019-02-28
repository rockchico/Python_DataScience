x = [3,5,1,8,2]
y = sorted(x)

print("x = ", x)
print("y = ", y)

x.sort()

print("x = ", x)


#	sort	the	list	by	absolute	value	from	largest	to	smallest
x = sorted([-4,1,-2,3],	key=abs,	reverse=True)		#	is	[-4,3,-2,1]
#	sort	the	words	and	counts	from	highest	count	to	lowest
wc = sorted(y.items(), key=lambda	(word,	count):	count, reverse=True)