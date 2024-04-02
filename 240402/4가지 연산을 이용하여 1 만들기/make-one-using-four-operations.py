from collections import deque

n = int(input())

visited = [False] * (n + 3)
step = [0] * (n + 3)

def in_range(x):
    return x >= 0 and x < n + 3

def can_go(x):
    if not in_range(x) or visited[x]:
        return False
    return True

def push(x, s):
    visited[x] = True
    step[x] = s
    q.append(x)

def bfs():
    while q:
        x = q.popleft()

        if can_go(x * 3):
            push(x * 3, step[x] + 1)
        if can_go(x * 2):
            push(x * 2, step[x] + 1)
        if can_go(x + 1):
            push(x + 1, step[x] + 1)
        if can_go(x - 1):
            push(x - 1, step[x] + 1)

q = deque()
q.append(1)
bfs()
print(step[n])