import itertools
import math
import re
from advent import Session
aoc = Session(2020,2)

with aoc.fp() as f:
	L = f.readlines()

silver = 0
gold = 0
regex = r"(\d+)-(\d+) ([a-zA-Z]): ([a-zA-Z]+)"

def getChar(i,s): 
	if(1 <= i <= len(s)):
		return s[i-1]
	return '?'

for line in L:
	n1,n2,letter,password = re.match(regex,line).groups()

	n1,n2 = int(n1),int(n2)
	c1,c2 = getChar(n1,password),getChar(n2,password)

	if n1 <= password.count(letter) <= n2:
		silver += 1

	if (c1 == letter) ^ (c2 == letter):
		gold += 1

print("silver:",silver)
print("gold:",gold)
