from nltk.parse.generate import generate
from nltk import CFG
import time

def postfix_grammar():#digits):
	grammar = [
	"S -> E E W",
	"E -> E E W | N",
	"W -> 'ω'",
	"N -> '#'"
	]
	# for d in digits:
	# 	grammar.append(f"N -> '{d}'")
	return CFG.fromstring(grammar)

number = "1234"

grammar = postfix_grammar()
print("\n", grammar, "\n")

words = list(generate(grammar, depth=6))
for word in words:
	if sum(1 for t in word if t == "#") == len(number):
		print(''.join(word))

# for d in range(0,10):

# 	start = time.time()

# 	sentences = list(generate(grammar, depth=d))
# 	#count = 0
# 	max_len = 0
# 	max_w = 0
# 	for s in sentences:
# 		# print(s)
# 		if len(s) > max_len:
# 			max_len = len(s)
# 		if sum(1 for t in s if t == 'ω') > max_w:
# 			max_w = sum(1 for t in s if t == 'ω')
# 	print(f"d = {d}")
# 	print(f"longest sentence: {max_len}")
# 	print(f"most operators: {max_w}")
# 	#	if sum(1 for t in s if t == '#') == 2:
# 	#		print(s)
# 	#		count += 1
# 	#print(f"total: {count}")

# 	print(f"Time taken: {time.time()-start}''")

# depth 9 ((est.) 63 operators, 2.5 hours to run)
# depth 8 for 6 digits (max len 63 (!), 31 operators, 12 seconds to run)
# depth 7 for 5 digits (max len 31, 15 operators, 0.017 seconds to run)
# depth 6 for 4 digits (max len 15, 7 operators, <0.001 seconds)
# depth 5 for 3 digits (max len 7, 3 operators, <0.001 seconds)
# depth 4 for 2 digits (max len 3, 1 operator, <e^-5 seconds)
# depth <4 for none (max len 0)


"""
S -> E E W
E -> E E W | N
W -> 'w'
N -> 'N'
W -> '+' | '-' | '×' | '÷'
N -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
"""