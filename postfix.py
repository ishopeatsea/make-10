from nltk.parse.generate import generate#, demo_grammar
from nltk import CFG

#grammar = CFG.fromstring(demo_grammar)
#print(demo_grammar)
#print(grammar)
postfix_grammar = """
S -> E E W
E -> E E W | N
W -> '+' | '-' | '×' | '÷'
N -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
"""
#print(postfix_grammar)
grammar = CFG.fromstring(postfix_grammar)
print(grammar)

sentences = list(generate(grammar, depth=4))
print([s for s in sentences])




#from collections import deque
#from random import random

#def generate_wordspace(n): # n = number of digitsl
#	if n < 2:
#		raise Exception("n must be >= 2")
#	
#	wcount = 1
#	#q = deque("EEW")
#	q = deque(['E', 'E', 'W'])
#	while wcount < n-1:
#		t = q.popleft()

#	ncount = 0
#	wcount = 1
#	result = []
#	q = deque(['E', 'E', 'W'])
#	while ncount < 4:
#		#print(string.popleft())
#		t = q.popleft()
#		if t == 'N' or t == 'W':
#			result.append(t)
#		elif wcount == n-1:
#			q.appendleft('N')
#		else:
#			pass
#		ncount += 1
#	
#generate_postfix(1)
#	
#	def parse(t): # token
#		if token == 'S':
#			return 'EEW'
#		elif token == 'E':
#			if random() < 0.5:
#				return 'EEW'
#			else:
#				return 'N'
#				
#	
#def parse_grammar_token(token):
#	if token == 'S':
#		return 'EEW'
#	else:
#		return 'N'

"""
S -> E E W
E -> E E W | N
W -> 'w'
N -> 'N'
W -> '+' | '-' | '×' | '÷'
N -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
"""