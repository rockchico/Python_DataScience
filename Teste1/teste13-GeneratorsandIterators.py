def	lazy_range(n):
    """a	lazy	version	of	range"""
    i	=	0
    while	i	<	n:
        yield	i
        i	+=	1


for	i	in	lazy_range(10):
    print(i)