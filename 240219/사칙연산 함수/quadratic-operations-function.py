def add(a, b):
    return f'{a} {o} {b} = {a + b}'

def sub(a, b):
    return f'{a} {o} {b} = {a - b}'

def div(a, b):
    return f'{a} {o} {b} = {a // b}'

def mul(a, b):
    return f'{a} {o} {b} = {a * b}'

a, o, c = input().split()

a, c = int(a), int(c)

if o == '+':
    print(add(a, c))
elif o == '-':
    print(sub(a, c))
elif o == '/':
    print(div(a, c))
elif o == '*':
    print(mul(a, c))
else:
    print('False')