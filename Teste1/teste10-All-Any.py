var1 = all([True,	1,	{	3	}])			#	True
print(var1)
var1 = all([True,	1,	{}])						#	False,	{}	is	falsy
print(var1)
var1 = any([True,	1,	{}])						#	True,	True	is	truthy
print(var1)
var1 = all([])																	#	True,	no	falsy	elements	in	the	list
print(var1)
var1 = any([])
print(var1)																	#	False,	no	truthy	elements	in	the	list