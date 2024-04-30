n = int(input())

d = dict()

for _ in range(n):
    direction = input().split()
    if direction[0] == 'add':
        d[direction[1]] = direction[2]
    elif direction[0] == 'find':
        if d.get(direction[1]):
            print(d.get(direction[1]))
        else:
            print('None')
    elif direction[0] == 'remove':
        d.pop(direction[1])