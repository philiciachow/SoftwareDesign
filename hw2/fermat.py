# Soft Des HW2 
# Think Python exercise 5-3


def check_fermat(a, b, c, n):
	if n <= 2:
		print "n must be greater than 2"
		return

	if a**n + b**n == c**n:
		print "Holy smokes, Fermat was wrong!" 
	else:
		print "No, that doesn't work."


a = int(raw_input('Enter an integer for a: '))
b = int(raw_input('Enter an integer for b: '))
c = int(raw_input('Enter an integer for c: '))
n = int(raw_input('Enter an integer for n: '))

check_fermat(a, b, c, n)