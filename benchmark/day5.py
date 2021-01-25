from advent import Session
import re

aoc = Session(2020,5)
with aoc.fp() as fp:
    L = [line.strip() for line in fp.readlines()]

def seatID(s):
    return int("".join([str(int(c in "BRAP")) for c in s]),2)
   
seats = [seatID(line) for line in L]
openSeats = [x for x in range(min(seats),max(seats)) if x not in set(seats)]
print("silver:",max(seats))
print("gold:",*openSeats)
