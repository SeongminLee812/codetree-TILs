import sys
from collections import deque

n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
INT_MIN = -sys.maxsize

dp = [
    [INT_MIN] * n
    for _ in range(n)
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def is_start(x, y):
    # 시작점인지 판단
    # 시작점 정의 : 다른 인접한 칸으로부터 흘러들어올 여지가 없는 포인트
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and arr[nx][ny] < arr[x][y]:
            return False
    return True

def can_go(x, y, threshold):
    if not in_range(x, y):
        return False
    if arr[x][y] <= threshold:
        return False
    return True

def push(x, y, s):
    dp[x][y] = s
    q.append((x, y))

q = deque()

for i in range(n):
    for j in range(n):
        if is_start(i, j):
            dp[i][j] = 1
            q.append((i, j))

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

while q:
    x, y = q.popleft()
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny, arr[x][y]):
            push(nx, ny, dp[x][y] + 1)


max_val = 0
for line in dp:
    max_val = max(max_val, max(line))
print(max_val)