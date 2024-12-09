#!/usr/bin/python3 
from z3 import * 

v3 = [BitVec(f'flag_{i}', 8) for i in range(63)]
solver = Solver()
# for i in range(63):
#     solver.add(v3[i] > 32)
#     solver.add(v3[i] < 127)

txt = open("lib.txt", "r").read().split('\n')
cnt = 0
mp = {}
for i in range(len(txt)):
    if 'EPFL' in txt[i]:
        functionName = txt[i][txt[i].index('E') : txt[i].index('(')]
        mp[functionName] = txt[i: i + 10]

list_func = open("list.txt", "r").read().split('\n')[:-1]
sub = []
cnt = 0
for x in list_func:
    expression = mp[x][-2]
    expression = expression[9:-1]
    
    if '*v3' in expression:
        expression = expression.replace('*v3', 'v3[0]')
        
    if '(unsigned __int8)' in expression:
        expression = expression.replace('(unsigned __int8)', '')
        # idx = expression.index('==')
        # new_expression = expression[:idx] + "& 0xff " + expression[idx:]
        # expression = new_expression
    cnt += 1 
    solver.add(eval(expression))


solver.add(v3[0] == ord('E'))
solver.add(v3[1] == ord('P'))
solver.add(v3[2] == ord('F'))
solver.add(v3[3] == ord('L'))
solver.add(v3[4] == ord('{'))
solver.add(v3[62] == ord('}'))
solver.add(v3[40] == ord('3'))
if solver.check() == sat:
    m = solver.model()
    arr = [m[v3[i]].as_long() for i in range(63)]
    print(bytes(arr))
