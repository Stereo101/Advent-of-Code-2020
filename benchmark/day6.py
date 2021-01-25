from advent import Session
import re

aoc = Session(2020,6)
with aoc.fp() as fp:
    L = fp.read().split("\n\n")

silver,gold = 0,0
for group in L:
    everyone = set("abcdefghijklmnopqrstuvwxyz")
    anyone = set()

    for person in group.split("\n"):
        everyone &= set(person)
        anyone |= set(person)
        
    silver += len(anyone)
    gold += len(everyone)
print("silver:",silver)
print("gold:",gold)
