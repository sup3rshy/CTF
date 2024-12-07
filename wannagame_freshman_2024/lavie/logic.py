#!/usr/bin/python3

command = open("command", "rb").read()

inp = [f'inp_{i}' for i in range(0x20)]
type_command = command[0] - 17 
idx_command = 1 
idx_input = 0
return_value = 0 
stack = []

while True:
    if type_command == 9:
        break 
    if type_command == 0:
        print(f'0: stack[{len(stack)}] = {command[idx_command]}')
        stack.append(str(command[idx_command]))
        idx_command += 1 
    elif type_command == 1:
        assert(len(stack) > 0)
        print(f'1: return_value = {stack[-1]}')
        return_value = stack.pop()
    elif type_command == 2:
        assert(len(stack) > 1)
        x = stack.pop()
        y = stack.pop()
        x = f'{x} * {y}'
        print(f'2: {x}')
        stack.append(x)
    elif type_command == 3:
        assert(len(stack) > 1)
        x = stack.pop()
        y = stack.pop()
        x = f'{x} + {y}'
        print(f'3: {x}')
        stack.append(x)
    elif type_command == 4:
        print(f'4: return_value = {return_value}')
    elif type_command == 5:
        print(f'5: stack push {inp[idx_input]}')
        stack.append(inp[idx_input])
    elif type_command == 6:
        assert(len(stack) > 1)
        v22 = stack.pop()
        v23 = stack.pop()
        x = f'(({v23} >> {v22}) & 1)'
        stack.append(x)
        print(f'6: {x}')
    elif type_command == 7:
        assert(len(stack) > 1)
        x = stack.pop()
        y = stack.pop()
        x = f'({x} ^ {y})'
        print(f'7: {x}')
        stack.append(x)
    elif type_command == 8:
        idx_input += 1
        
    type_command = command[idx_command] - 17 
    idx_command += 1 
    assert(type_command <= 9)
