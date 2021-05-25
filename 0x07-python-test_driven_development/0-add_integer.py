#!/usr/bin/python3

""" function to adds 2 integers"""


def add_integer(a, b=98):

	""" adds 2 integers a and b
	>>> add_integer(5, 98)
	103
	>>> add_integer(-5, 98)
	93
	"""
	if type(a) not in [int, float]:
		raise TypeError ('a must be an integer')
	elif type(a) is float:
		a = int(a)
	if type(b) not in [int, float]:
		raise TypeError ('b must be an integer')
	elif type(b) is float:
		b = int(b)
	return a + b

if __name__ == "__main__":
	import doctest
	doctest.testfile("tests/0-add_integer.txt")
