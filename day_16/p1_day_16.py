import sys
sys.setrecursionlimit(100000)
data = open('16').read().split('\n')

grid = {}
dirs = ((1,0),(-1,0),(0,1),(0,-1))
tsplit = set()
for r,l in enumerate(data):
    for c,v in enumerate(l):
        grid[(r,c)] = v
        if v == 'S':
            start = (r,c)
        if v == 'E':
            end = (r,c)
        cnt = 0
        if v == '.':
            for dr,dc in dirs:
                if data[r+dr][c+dc] == '.':
                    cnt += 1
        if cnt > 3:
            tsplit.add((r,c))

seen = set()

distanceMap = {(start):0}
state = (start,(0,1))
seen.add(state)
def solve(p=start,d=(0,1),dis=0,steps=1):
    res = [1E20] 
    paths = [{start}]
    r,c = p
    path = {(r,c)}
    if grid[(r,c)] == 'E':
            print(dis)
            return dis,path
    for dr,dc in dirs:
        nr,nc = r+dr,c+dc
        if grid[(nr,nc)] == 'E':
            return dis+1,path
        if grid[(nr,nc)] == '.' and d != (-dr,-dc):
            distance = dis+1 if d == (dr,dc) else dis+1001
            if ((nr,nc),(dr,dc)) in seen and distanceMap[(nr,nc)]+1000 < distance: continue
            seen.add(((nr,nc),(dr,dc)))
            distanceMap[(nr,nc)] = distance
            if d == (dr,dc):
                a,b = solve((nr,nc),(dr,dc),distance,steps+1)
            else:
                a,b = solve((nr,nc),(dr,dc),distance,steps+1)
            res.append(a)
            paths.append(b)
    score = min(res)
    for i,v in enumerate(res):
        if v == score:
            path = path|paths[i]
    return score,path

a,b = solve()
print(a)
print(len(b)+1)


# ll = ''
# for r,l in enumerate(data):
#     for c,v in enumerate(l):
#         if (r,c) in b:
#             ll += 'O'
#         else:
#             ll += v
#     ll += '\n'

# print(ll)