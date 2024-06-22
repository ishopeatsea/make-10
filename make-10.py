from enum import StrEnum
from itertools import permutations, product #pairwise, starmap
# import numpy as np

def printlist(list):
	for x in list:
		print(x)
def printsoln(list):
	for (a,b,c,d), (f,g,h) in list:
		print(a,w(f),b,w(g),c,w(h),d,"= 10")

def add(x,y):
	return x+y
def subtract(x,y):
	return x-y
def multiply(x,y):
	return x*y
def divide (x,y):
	return x/y
def funclist():
	return [
		add,
		subtract,
		multiply,
		divide
	]
def w(f): # ω is the symbol used in the definition of "operation" - https://en.m.wikipedia.org/wiki/Operation_(mathematics)#Definition 
	return {
		'add': '+',
		'subtract': '-',
		'multiply': '×',
		'divide': '÷',
	}[f.__name__]

def split_digits(input):
	return [int(c) for c in str(input)]
	
funcs = funclist()
number = input("Carriage number: ")
digits = split_digits(number)
tens = []
for a, b, c, d in permutations(digits, 4):
	for f, g, h in product(funcs, repeat=3):
		try:
			if h(g(f(a,b),c),d) == 10:
				tens.append(((a,b,c,d),(f,g,h)))
		except ZeroDivisionError:
			#print("skipped - divide by zero")
			pass
printsoln(tens)