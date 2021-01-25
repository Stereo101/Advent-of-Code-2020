from advent import Session
from hashlib import md5
import math
import itertools

aoc = Session(2020,16)

with aoc.fp() as fp:
    L = [line.strip() for line in fp.readlines()]
silver,gold = 0,0
 
index = 0
rules = []
anyN = set()
while "your ticket" not in L[index]:
    if(L[index] == ""):
        index += 1
        continue
    r,ranges = L[index].split(": ")
    a = []
    for x in ranges.split(" or "):
        start,end = x.split("-")
        start,end = int(start),int(end)
        for i in range(start,end+1):
            anyN.add(i)
        a.append((start,end))
    rules.append([r,a])
    index += 1

index += 1
yourTicket = L[index]
index += 3

nearby = []
while index < len(L):
    nearby.append(L[index])
    index += 1

invalid = 0
validTickets = []
for ticket in nearby:
    z = invalid
    for n in ticket.split(","):
        if int(n) not in anyN:
            invalid += int(n)
            break
    if(invalid == z):
        validTickets.append(ticket)
silver = invalid
            

rulePasses = {}
ticketLen = len(yourTicket.split(","))
for rule in rules:
    for i in range(ticketLen):
        passing = True
        for ticket in validTickets:
            n = int(ticket.split(",")[i])
            if(rule[1][0][0] <= int(n) <= rule[1][0][1] or rule[1][1][0] <= int(n) <= rule[1][1][1]):
                continue
            else:
                passing = False
                break
        if(passing):
            rulePasses[rule[0]] = rulePasses.get(rule[0],[]) + [i]

rPass = [(k,v) for k,v in rulePasses.items()]
rPass.sort(key=lambda x:len(x[1]))
ruleOrder = []
used = set()
v = 1
for i in [3,6,7,9,14,16]:
    v *= int(yourTicket.split(",")[i])
gold = v

print("silver:",silver)
print("gold:",gold)
