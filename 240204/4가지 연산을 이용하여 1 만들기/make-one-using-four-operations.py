from collections import deque

n = int(input())

visited = [False] * (n + 3)
step = [0] * (n + 3)

def in_range(x):
    return x >= 0 and x <= n + 2

def can_go(x):
    if not in_range(x):
        return False
    if visited[x]:
        return False
    return True

def push(x, v):
    global q, visited, step
    visited[x] = True
    q.append(x)
    step[x] = v

def bfs():
    global q, visited

    while q:
        x = q.popleft()
        if x % 3 == 0:
            nx = x // 3
            if can_go(nx):
                push(nx, step[x] + 1)
        if x % 2 == 0:
            nx = x // 2
            if can_go(nx):
                push(nx, step[x] + 1)
        nx = x + 1
        if can_go(nx):
            push(nx, step[x] + 1)
        nx = x - 1
        if can_go(nx):
            push(nx, step[x] + 1)

        if step[1]:
            print(step[1])
            return

q = deque()
q.append(n)
visited[n] = True
bfs()