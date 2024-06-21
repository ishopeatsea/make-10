from enum import Enum
from itertools import permutations #pairwise, starmap
# import numpy as np

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
abcd = split_digits(1234)
tree = {}
for a, b in permutations(abcd, 2):
	print(a,b)
	tree[a,b] = {}
	tree[a,b]['slag'] = [x for x in abcd if x not in [a,b]]
	tree[a,b]['funcs'] = {}
	for f in funcs:
		fnym = f.__name__
		tree[a,b]['funcs'][fnym] = {}
		tree[a,b]['funcs'][fnym]['result'] = f(a,b)
	for c in tree[a,b]['slag']:
		for f, branch in tree[a,b]['funcs'].items():
			tree[a,b]['funcs'][f]['next'] = {}
			for g in funcs:
				gnym = g.__name__
# fuck this

# for x in permutations(digits, 2):
# 	for f in funcs: 
# 		print(f"{f.__name__}{x} = {f(x[0], x[1])}")