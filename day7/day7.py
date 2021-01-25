from advent import Session
import re

aoc = Session(2020,7)
with aoc.fp() as fp:
    #L = fp.read().split("\n\n")
    L = [line.strip() for line in fp.readlines()]

bag_dict = {}
for line in L:
    bag,contains = line[:-1].split("s contain ")
    contain_dict = {}
    if(contains != "no other bags"):
        for cBag in contains.split(", "):
            n,cb = cBag.split(" ",1)
            if(cb.endswith("s")):
                cb = cb[:-1]
            contain_dict[cb] = int(n)
    bag_dict[bag] = contain_dict

#find all bags which contain shiny gold
contains = set()
changed = True
while changed:
    changed = False
    for bag in bag_dict.keys() - contains:
        if("shiny gold bag" in bag_dict[bag] or any(c in bag_dict[bag] for c in contains)):
            contains.add(bag)
            changed = True

memo = {}
def count_bag(bag,d):
    if(bag not in memo):
        memo[bag] = 0 if len(d[bag]) == 0 else sum(v*(1+count_bag(k,d)) for k,v in d[bag].items())
    return memo[bag]
print("silver:",len(contains))
print("gold:",count_bag("shiny gold bag",bag_dict))
