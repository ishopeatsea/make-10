from nltk.parse.generate import generate
from nltk import CFG

postfix_grammar = """
S -> E E W
E -> E E W | N
W -> 'ω'
N -> '#'
"""
grammar = CFG.fromstring(postfix_grammar)
print(grammar)

sentences = list(generate(grammar, depth=8))
#count = 0
max = 0
for s in sentences:
	print(s)
	if len(s) > max:
		max = len(s)
print(f"longest sentence: {max}")
#	if sum(1 for t in s if t == '#') == 2:
#		print(s)
#		count += 1
#print(f"total: {count}")

# depth 8 for 6 digits (max len 63 (!))
# depth 7 for 5 digits (max len 31)
# depth 6 for 4 digits (max len 15)
# depth 5 for 3 digits (max len 7)
# depth 4 for 2 digits (max len 3)
# depth 3 for none (max len 0)


"""
S -> E E W
E -> E E W | N
W -> 'w'
N -> 'N'
W -> '+' | '-' | '×' | '÷'
N -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
"""