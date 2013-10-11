def do_twice(f,s):
	f(s)
	f(s)

def print_twice(x):
	print x
	print x

def do_four(g, y):
	do_twice(g,y)
	do_twice(g,y)


do_four(print_twice, 'spam')