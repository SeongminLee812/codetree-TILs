from collections import deque

q = deque()

n = int(input())

for _ in range(n):
    d = input().split()
    if d[0] == 'push':
        q.append(d[1])
    elif d[0] == 'pop':
        print(q.popleft())
    elif d[0] == 'size':
        print(len(q))
    elif d[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    else:
        print(q[0])