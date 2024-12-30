import numpy as np
import tqdm

with open('2024_20.txt') as f:
    grid = np.array([list(line) for line in f.read().splitlines()])
    
ishape,jshape = grid.shape

start = [(i,j) for i,line in enumerate(grid) for j,char in enumerate(line) if char=='S']
assert len(start)==1
start = start[0]
end = [(i,j) for i,line in enumerate(grid) for j,char in enumerate(line) if char=='E']
assert len(end)==1
end = end[0]

track = {start:0}
cur = start
curstep = 0
while cur != end:
    curstep += 1
    i,j = cur
    for di,dj in [[-1,0],[0,-1],[0,1],[1,0]]:
        newi,newj = i+di,j+dj
        if (newi,newj) not in track and grid[newi][newj] in 'SE.':
            cur = (newi,newj)
            track[cur] = curstep
            break

def cheat_endpoints(coords):
    i,j = coords
    output = set()
    for di in range(-20,21):
        djmax = 20-abs(di)
        for dj in range(-djmax,djmax+1):
            if (i+di,j+dj) in track:
                output.add((i+di,j+dj))
    return output

def manhattan_distance(coord1,coord2):
    return sum(abs(i-j) for i,j in zip(coord1,coord2))

count = 0
for coords in track:
    potentials = cheat_endpoints(coords)
    for othercoords in potentials:
        if track[othercoords]-track[coords]-manhattan_distance(coords,othercoords) >= 100:
            count += 1

print(count)