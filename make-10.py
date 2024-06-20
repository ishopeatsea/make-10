from enum import Enum
from itertools import permutations #pairwise, starmap

def add(x,y):
	return x+y
def subtract(x,y):
	return x-y
def multiply(x,y):
	return x*y
def divide (x,y):
	return x/y

def split_digits(input):
	return [int(c) for c in str(input)]
	
funcs = [
	add,
	subtract,
	multiply,
	divide
]
digits = split_digits(1234)
for x in permutations(digits, 2):
	for f in funcs: 
		print(f"{f.__name__}{x} = {f(x[0], x[1])}")