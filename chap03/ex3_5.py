def first_line(x):
	for i in range(x):
		print '+',
		print '-'*4,
	print '+'

def second_line(x):
	for i in range(4):
		for i in range(x):
			print '|',
			print ' '*4,
		print '|'


def draw_grid(num_col, num_rows):
	for i in range(num_rows):
		first_line(num_col)
		second_line(num_col)
	first_line(num_col)


draw_grid(4,4)