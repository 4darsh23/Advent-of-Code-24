data = open('10').read().split('\n')

kaart = {}
queue = []
for r,line in enumerate(data):
    for c,v in enumerate(line):
        kaart[(r,c)] = int(v)
        if v == '0':    
            queue.append((r,c))

dirs = ((-1,0),(1,0),(0,1),(0,-1))

def travel(x,part=1):
    route = [x]
    ends = 0
    for r,c in route:
        h = kaart[(r,c)]
        for dr,dc in dirs:
            nr,nc = r+dr,c+dc
            if (nr,nc) in kaart and kaart[(nr,nc)] == h+1:
                if part == 1:
                    if (nr,nc) not in route: 
                        route.append((nr,nc))
                        if h + 1 == 9:
                            ends += 1
                if part == 2:
                    route.append((nr,nc))
                    if h + 1 == 9:
                        ends += 1
    return ends

p1 = p2 = 0
for i in queue:
    p1 += travel(i,1)
    p2 += travel(i,2)
print(p1)
print(p2)