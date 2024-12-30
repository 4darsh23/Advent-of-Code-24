Registers,program = open('17').read().split('\n\n')

regs = [int(i) for i in Registers.split()[2::3]]
program = [int(i) for i in program.split(' ')[1].split(',')]

def computer(regs):
    ptr = 0
    output = []
    while ptr < len(program):
        ins,op = program[ptr:ptr+2]
        if  0<=op<=3:  combo = op
        elif op == 4:  combo = regs[0]
        elif op == 5:  combo = regs[1]
        elif op == 6:  combo = regs[2]

        if   ins == 0: regs[0] = regs[0]//2**combo
        elif ins == 1: regs[1] = regs[1]^op
        elif ins == 2: regs[1] = combo%8
        elif ins == 3: ptr = ptr+2 if regs[0] == 0 else op-2
        elif ins == 4: regs[1] = regs[1]^regs[2]
        elif ins == 5: output.append(combo%8)
        elif ins == 6: regs[1] = regs[0]//2**combo
        elif ins == 7: regs[2] = regs[0]//2**combo
        ptr += 2
    return output

print(','.join([str(i) for i in computer(regs)]))

def solve(n=0,d=15):
    res = [1E20]
    if d == -1: return n
    for i in range(8):
        nn = n+i*8**d
        regs = [nn,0,0]
        output = computer(regs)
        if len(output) != len(program):continue
        if output[d] == program[d]: res.append(solve(nn,d-1))
    return min(res)

print(solve())