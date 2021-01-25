from advent import Session
import math

aoc = Session(2020,20)

with aoc.fp() as fp:
    L = [line.strip() for line in fp.readlines()]
silver,gold = 0,0

i = 0
tiles = {}
while i < len(L):
    n = int(L[i].split("Tile ")[1].split(":")[0])
    k = 1
    g = []
    while L[k+i] != "":
        g.append(tuple(L[k+i]))
        k += 1
    tiles[n] = g
    i += k+1

def get_sides(tile):
    height = len(tile)
    width = len(tile[0])
    
    edges = []
    edges.append(tuple(tile[0][x] for x in range(width)))
    edges.append(tuple(tile[height-1][x] for x in range(width)))
    edges.append(tuple(tile[y][width-1] for y in range(height)))
    edges.append(tuple(tile[y][0] for y in range(height)))

    return [max(e,tuple(reversed(e))) for e in edges]

def rrot(tile):
    return tuple(zip(*tile[::-1]))

def flip_right(tile):
    return tuple(tuple(reversed(line)) for line in tile)

def flip_top(tile):
    return tuple(reversed(tile))
    
def rrot_multi(tile,rots):
    t = tile
    for _ in range(rots%4):
        t = rrot(t)
    return t

def rrot_match_right(t1,t2):
    height = len(t1)
    width = len(t1[0])

    for t1_rot in range(4):
        right_edge = tuple(t1[y][width-1] for y in range(height))
        for t2_rot in range(4):
            left_edge = tuple(t2[y][0] for y in range(height))
            if(right_edge == left_edge):
                return t1_rot,t2_rot,0
            elif(tuple(reversed(right_edge)) == left_edge):
                return t1_rot,t2_rot,1
            t2 = rrot(t2)
        t1 = rrot(t1)
    return -1,-1,-1

def rrot_match_down(t1,t2):
    height = len(t1)
    width = len(t1[0])

    for t1_rot in range(4):
        bottom_edge = tuple(t1[height-1][x] for x in range(width))
        for t2_rot in range(4):
            top_edge = tuple(t2[0][x] for x in range(width))
            if(bottom_edge == top_edge):
                return t1_rot,t2_rot,0
            elif(tuple(reversed(bottom_edge)) == top_edge):
                return t1_rot,t2_rot,1
            t2 = rrot(t2)
        t1 = rrot(t1)
    return -1,-1,-1
   
def get_tile_grid(tiles,relations):
    placed = set()
    seen = set()
    frontier = []
    
    tile_grid = []
    side_len = int(len(tiles)**.5)
    for _ in range(side_len):
        tile_grid.append([-1] * side_len)

    #find a corner
    for t,v in relations.items():
        if(len(v) == 2):
            first_corner = t
            break
    
    placed.add(first_corner)
    frontier.append((first_corner,0,0))
    
    while frontier:
        t1_n,x,y = frontier.pop(0)
        t1 = tiles[t1_n]
        to_place = [r for r in relations[t1_n] if r not in placed]
        if len(to_place) == 2:
            t2_n,t3_n = to_place
            t2,t3 = tiles[t2_n],tiles[t3_n]

            t1t2_rot,t2_rot,t2_flip = rrot_match_right(t1,t2)
            t1t3_rot,t3_rot,t3_flip = rrot_match_down(t1,t3)
            #tiles are swapped if t1t2_rot != t1t3_rot
            #only occurs during orientation of first corner
            if(t1t2_rot != t1t3_rot or t1t2_rot == -1 or t1t3_rot == -1):
                t2,t3 = t3,t2
                t2_n,t3_n = t3_n,t2_n
                t1t2_rot,t2_rot,t2_flip = rrot_match_right(t1,t2)
                t1t3_rot,t3_rot,t3_flip = rrot_match_down(t1,t3)

            if(t2_n not in seen):
                frontier.append((t2_n,x+1,y))
            if(t3_n not in seen):
                frontier.append((t3_n,x,y+1))
            t2 = flip_top(rrot_multi(t2,t2_rot)) if t2_flip else rrot_multi(t2,t2_rot)
            t3 = flip_right(rrot_multi(t3,t3_rot)) if t3_flip else rrot_multi(t3,t3_rot)
            assert t1_n == first_corner or t1t3_rot == t1t2_rot == 0

            seen.add(t2_n)
            seen.add(t3_n)
            t1 = rrot_multi(t1,t1t2_rot)
            tiles[t1_n] = t1
            tiles[t2_n] = t2
            tiles[t3_n] = t3
        elif len(to_place) == 1:
            match_right = False
            match_down = False

            #at boundary?
            if(x == side_len-1):
                match_down = True
            elif(y == side_len-1):
                match_right = True
            elif(tile_grid[y][x+1] == -1):
                match_right = True
            elif(tile_grid[y+1][x] == -1):
                match_down = True

            t2_n = to_place[0]
            t2 = tiles[t2_n]
            if(match_right):
                t1_rot,t2_rot,t2_flip = rrot_match_right(t1,t2)
                nx,ny = x+1,y
            else:
                t1_rot,t2_rot,t2_flip = rrot_match_down(t1,t2)
                nx,ny = x,y+1

            assert t1_rot == 0
            t2 = rrot_multi(t2,t2_rot)
            if(t2_flip):
                t2 = flip_top(t2)
            if(t2_n not in seen):
                frontier.append((t2_n,nx,ny))

            tiles[t2_n] = t2
            seen.add(t2_n)
        
        tile_grid[y][x] = t1_n
        placed.add(t1_n)
    return tile_grid

def tile_center(tile):
    new_tile = []
    for y in range(1,len(tile)-1):
        new_tile.append([tile[y][x] for x in range(1,len(tile[0])-1)])
    return new_tile

def create_mega_grid(tile_grid,tiles):
    mega_grid = []
    for y in range(len(tile_grid)):
        row = tile_center(tiles[tile_grid[y][0]])
        for tile_n in tile_grid[y][1:]:
            center = tile_center(tiles[tile_n])
            for i,line in enumerate(center):
                row[i] += line
        for r in row:
            mega_grid.append(r)
    return mega_grid
                
            
def search_for_pattern(pattern,grid):
    pattern_height = len(pattern)
    pattern_width = len(pattern[0])
    grid_height = len(grid)
    grid_width = len(grid[0])

    touched = set()
    match_index = []
    for y in range(grid_height-pattern_height):
        for x in range(grid_width-pattern_width):
            matching = True
            maybe_touched = set()
            for py in range(pattern_height):
                for px in range(pattern_width):
                    ax = x+px
                    ay = y+py
                    if(pattern[py][px] != " " and grid[ay][ax] != pattern[py][px]):
                        matching = False
                        break
                    elif(pattern[py][px] == "#"):
                        maybe_touched.add((ax,ay))
                    
                if(not matching):
                    break
            if(matching):
                match_index.append((x,y))
                touched |= maybe_touched
    return match_index,len(touched)

monster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.split("\n")
monster = [list(x) for x in monster]

monster_rev = flip_right(monster)
monster_group = []
for i in range(4):
    monster_group.append(rrot_multi(monster,i))
    monster_group.append(rrot_multi(monster_rev,i))
    
edge_tiles = {}
for n,t in tiles.items():
    for edge in get_sides(t):
        d = edge_tiles.get(edge,set())
        d.add(n)
        edge_tiles[edge] = d
        
relations = {}
for tile_set in edge_tiles.values():
    for n in tile_set:
        s = relations.get(n,set())
        s |= tile_set - {n}
        relations[n] = s


tile_grid = get_tile_grid(tiles,relations)
mega_grid = create_mega_grid(tile_grid,tiles)

most_touched = 0
for monster in monster_group:
    index_list,touched = search_for_pattern(monster,mega_grid)
    most_touched = max(most_touched,touched)

silver = math.prod(tile_n for tile_n,neighbors in relations.items() if len(neighbors) == 2)
gold = str(mega_grid).count("#") - most_touched
    
"""
for line in mega_grid:
    print("".join(line))

for line in tile_grid:
    print(line)
"""
print("silver:",silver)
print("gold:",gold)
