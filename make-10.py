# from enum import StrEnum
from itertools import permutations, product #pairwise, starmap
# import numpy as np
from nltk.parse.generate import generate
from nltk import CFG
# from collections import deque

def printlist(list):
	for x in list:
		print(x)
# def printsoln(list):
# 	for (a,b,c,d), (f,g,h) in list:
# 		print(a,w(f),b,w(g),c,w(h),d,"= 10")

def count(thing, list):
	count = 0
	for x in list:
		if x == thing:
			count += 1
	return count

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

def postfix_grammar():
	postfix_grammar = """
	S -> E E W
	E -> E E W | N
	W -> 'ω'
	N -> '#'
	"""
	return CFG.fromstring(postfix_grammar)

# https://stackoverflow.com/a/30067622
def eval_postfix(string):
	s = [] # stack
	for t in string: # char
		if c in "0123456789":
			s.append(int(c))
		expr = None
		if not s.is_empty():



def get_number():
	return input("Carriage number: ")
# def split_digits(input):
# 	return [int(c) for c in str(input)]
	
def find_solutions(number, functions, target):

	grammar = postfix_grammar()
	sentences = [x for x in list(generate(grammar, depth=6)) if sum(1 for t in x if t == "#") == len(number)]
	numorders = permutations(number, 4)
	# funcorders = product(functions, repeat=3)
	# funcorders = product([w(f) for f in functions], repeat=3)

	solns = []
	#funcs = funclist()
	#number = input("Carriage number: ")
	# digits = split_digits(number)
	# for word in words:
	# 	print(''.join(word))
	# for perm in permutations(number, 4):
		# print(f"{''.join(perm)}")
	
	# for sentence,digits,funcs in list(product(sentences, numorders, funcorders)):
	for sentence,digits in list(product(sentences, numorders)):
		
		s = ''.join(sentence)
		s = s.replace('#',"{}").format(*digits)
		s = s.replace('ω',"{}").format(*product(functions, repeat=count('ω', s)))

		eval_postfix(s)

		solns.append(s)

		# for f, g, h in product(funcs, repeat=3):
		# 	try:
		# 		if h(g(f(a,b),c),d) == target:
		# 			solns.append(((a,b,c,d),(f,g,h)))
		# 	except ZeroDivisionError:
		# 		#print("skipped - divide by zero")
		# 		pass
	#printsoln(tens)
	return solns
	
if __name__ == "__main__":
	printlist(find_solutions(get_number(), funclist(), 10))
	# number = get_number()
	# while number != "exit":
	# 	printsoln(find_solutions(number, funclist(), 10))
	# 	number = get_number()