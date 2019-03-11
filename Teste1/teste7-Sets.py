s = set()
s.add(1) 
s.add(2)
s.add(2)

x = len(s)

y = 2 in s
z = 3 in s

print("x = ", x)
print("y = ", y)
print("z = ", z)

item_list	=	[1,	2,	3,	1,	2,	3]
num_items	=	len(item_list)																#	6
item_set	=	set(item_list)																	#	{1,	2,	3}
num_distinct_items	=	len(item_set)								#	3
distinct_item_list	=	list(item_set)							#	[1,	2,	3]