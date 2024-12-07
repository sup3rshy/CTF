#!/usr/bin/python3 

command = open("logic.txt", "r").read().split('\n')
condition_arr = []
for x in command:
    if '7: ' in x:
        condition_arr.append(x[3:])

ans = []
for i in range(0x20):
    current_inp = f'inp_{i}'
    for c in range(33, 127):
        text = condition_arr[i]
        text = text.replace(current_inp, str(c))
        if eval(text) == 0:
            ans.append(c)
            break 
print(bytes(ans))
