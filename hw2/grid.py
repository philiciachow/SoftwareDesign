# Soft Des HW2 
# Think Python exercise 3-5

# 2x2 square

def twice(f):
	f()
	f()

def four_times(f):
	twice(f)
	twice(f)

def print_sequence():
	print '+ - - - -', 

def print_beam():
	print '|        ', 

def print_sequences():
	twice(print_sequence)
	print '+'

def print_beams():
	twice(print_beam)
	print '|'

def print_row():
	print_sequences()
	four_times(print_beams)

def print_square():
	twice(print_row)
	print_sequences()

print_square()


# 4x4 square

def sequence(f, g, h):
	f()
	four_times(g)
	h()

def print_plus():
	print '+',

def print_minus():
	print '-',

def print_rod():
	print '|',

def print_space():
	print ' ',

def print_end():
	print

def nothing():
	"do nothing"

def print_one_row():
	sequence(nothing, print_minus, print_plus)

def print_one_column():
	sequence(nothing, print_space, print_rod)

def print_four_rows():
	sequence(print_plus, print_one_row, print_end)

def print_four_columns():
	sequence(print_rod, print_one_column, print_end)

def print_section():
	sequence(nothing, print_four_columns, print_four_rows)

def print_grid():
	sequence(print_four_rows, print_section, nothing)

print_grid()

# reference to Allen's code in Think Python