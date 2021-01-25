from advent import Session
import math
import itertools

aoc = Session(2020,21)


with aoc.fp() as fp:
    L = [line.strip() for line in fp.readlines()]
silver,gold = 0,0


food_list = []
ingredient_dict = {}
allergen_set = set()
for food in L:
    allergens = []
    if("(contains" in food):
        food,allergens = food.split(" (contains ")
        allergens = set(allergens[:-1].split(", "))
        allergen_set |= allergens
    food = set(food.split(" "))
    for ingr in food:
        d = ingredient_dict.get(ingr,set())
        d |= set(allergens)
        ingredient_dict[ingr] = d
    food_list.append([food,allergens])
    
guess = {}
for comb_len in range(1,len(allergen_set)):
    for comb in itertools.combinations(allergen_set,comb_len):
        S = None
        for food,allergens in food_list:
            if(allergens == set(comb)):
                if(S is None):
                    S = food.copy()
                else:
                    S &= food
        if(S is not None):
            guess[comb] = S

for alg in allergen_set:
    if (alg,) not in guess:
        #build alg base
        S = None 
        for k,v in guess.items():
            if(alg in k):
                if(S is None):
                    S = v.copy()
                else:
                    S &= v
        guess[(alg,)] = S

for _ in range(20):
    #many -> 1
    for alg in (alg for alg in allergen_set if (alg,) in guess):
        for k,v in guess.items():
            if alg in k:
                guess[(alg,)] &= v
    
    #prune single-tons
    for alg in allergen_set:
        if((alg,) in guess):
            S = guess[(alg,)]
            if(len(S) == 1):
                for comb in guess.keys():
                    if(alg not in comb):
                        guess[comb] -= S


    #Superset restriction?
    for k,v in guess.items():
        for a,b in guess.items():
            sk,sa = set(k),set(a)
            if(sk.issuperset(sa)):
                guess[a] &= guess[k]
            elif(sa.issuperset(sk)):
                guess[k] &= guess[a]
        
possible = set()
for k,v in guess.items():
    if(len(k) == 1):
        possible |= v

count = 0
for food,_ in food_list:
    count += sum(1 for f in food if f not in possible)
silver = count

bad_food = []
for alg in sorted(list(allergen_set)):
    bad_food.append(*guess[(alg,)])
    assert(len(guess[(alg,)])==1)
gold = ",".join(bad_food)

print("silver:",silver)
print("gold:",gold)
