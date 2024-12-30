data = open('14').read().strip().split('\n')

robots = {}
for i,line in enumerate(data):
    p,v = line.split() 
    p = [int(i) for i in p.split('=')[1].split(',')]
    v = [int(i) for i in v.split('=')[1].split(',')]
    robots[i] = p+v

Y= 103
X = 101

pos = []
q1=q2=q3=q4=0
step = 100
for i in robots:
    x,y,dx,dy = robots[i]
    x=(x+step*dx)%(X)
    y=(y+step*dy)%(Y)
    pos.append((x,y))
    if x < X//2:
        if y < Y//2:
            q1 += 1
        elif y > Y//2:
            q2 += 1
    elif x > X//2:
        if y < Y//2:
            q3 += 1
        elif y > Y//2:
            q4 += 1

def run(step):
    pos = set()
    f = False
    for i in robots:
        x,y,dx,dy = robots[i]
        x=(x+step*dx)%(X)
        y=(y+step*dy)%(Y)
        pos.add((x,y))
    if len(pos) == len(data):
        f = True
    if f:
        l = ''
        for y in range(Y):
            r = ''
            for x in range(X):
                if (x,y) in pos:
                    r += '#'
                else:
                    r += '.'
            l += r
            l += '\n'
        
        print(l)
        return 1
    
i = 1
while True:
    t = run(i)
    i+=1
    if t == 1:
        print(q1*q2*q3*q4)
        print(i-1)
        break