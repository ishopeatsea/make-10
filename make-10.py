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

def get_number():
	return input("Carriage number: ")
def split_digits(input):
	return [int(c) for c in str(input)]
	
def find_solutions(number, funcs, target):
	#funcs = funclist()
	#number = input("Carriage number: ")
	digits = split_digits(number)
	solns = []
	for a, b, c, d in permutations(digits, 4):
		for f, g, h in product(funcs, repeat=3):
			try:
				if h(g(f(a,b),c),d) == target:
					solns.append(((a,b,c,d),(f,g,h)))
			except ZeroDivisionError:
				#print("skipped - divide by zero")
				pass
	#printsoln(tens)
	return solns
	
if __name__ == "__main__":
	number = get_number()
	while number != "exit":
		printsoln(find_solutions(number, funclist(), 10))
		number = get_number()