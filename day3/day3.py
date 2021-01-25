import math
import os
import sys
from queue import PriorityQueue
from advent import Session

aoc = Session(2020,3)
with aoc.fp() as fp:
    grid = [line.strip() for line in fp.readlines()]

def count_tree(dx, dy, grid):
	x,y,tree = 0,0,0
	while y < len(grid):
		tree += grid[y][x] == "#"
		x = (x+dx) % len(grid[0])
		y = (y+dy)
	return tree

slopes = ((1,1),(3,1),(5,1),(7,1),(1,2))
counts = [count_tree(dx,dy,grid) for dx,dy in slopes]
print("silver:",counts[1])
print("gold:",math.prod(counts))
