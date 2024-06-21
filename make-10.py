from enum import StrEnum
from itertools import permutations, product #pairwise, starmap
# import numpy as np

def printlist(list):
	for x in list:
		print(x)

def add(x,y):
	return x+y
def subtract(x,y):
	return x-y
def multiply(x,y):
	return x*y
def divide (x,y):
	return x/y

def w(f): # ω is the symbol used in the definition of "operation" - https://en.m.wikipedia.org/wiki/Operation_(mathematics)#Definition 
	return {
	'add': '+',
	'subtract': '-',
	'multiply': '×',
	'divide': '÷',
	}[f.__name__]

def split_digits(input):
	return [int(c) for c in str(input)]
	
funcs = [
	add,
	subtract,
	multiply,
	divide
]
number = input("Carriage number: ")
digits = split_digits(number)
#results = {}
tens = []
for a, b, c, d in permutations(digits, 4):
	#results[a,b,c,d] = {}
	for f, g, h in product(funcs, repeat=3):
		try:
			print(a, w(f), b, w(g), c, w(h), d, "=", h(g(f(a,b),c),d))
			#results[a,b,c,d][f,g,h] = h(g(f(a,b),c),d)
			if h(g(f(a,b),c),d) == 10:
				#tens.append((a,w(f),b,w(g),c,w(h),d))
				tens.append(((a,b,c,d),(w(f),w(g),w(h))))
		except ZeroDivisionError:
			print(a, w(f), b, w(g), c, w(h), d, "skipped - divide by zero")
printlist(tens)
	

# for x in permutations(digits, 2):
# 	for f in funcs: 
# 		print(f"{f.__name__}{x} = {f(x[0], x[1])}")