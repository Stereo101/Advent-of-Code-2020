import itertools
import math 
from advent import Session
aoc = Session(2020,1)

with aoc.fp() as fp:
	L = [int(x) for x in fp.readlines()]

def k_sum(L, k, target):
	num_set = set(L)
	for comb in itertools.combinations(L, k-1):
		compliment = target - sum(comb)
		if compliment in num_set and compliment not in comb:
			return comb + (compliment,)
	return None
		

print("silver:",math.prod(k_sum(L,2,2020)))
print("gold:",math.prod(k_sum(L,3,2020)))

