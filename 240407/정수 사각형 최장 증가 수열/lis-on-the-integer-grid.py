import sys
INT_MIN = -sys.maxsize
sys.setrecursionlimit(10)

n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

memo = [
    [INT_MIN] * n
    for _ in range(n)
]

visited = [
    [False] * n
    for _ in range(n)
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def is_start(x, y):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and arr[nx][ny] > arr[x][y]:
            return False
    return True

def get_max(x, y, threshold):
    if not in_range(x, y) or arr[x][y] > threshold:
        return INT_MIN

    if visited[x][y]:
        return memo[x][y]

    if is_start(x, y):
        memo[x][y] = 1
        return memo[x][y]

    if memo[x][y] != INT_MIN:
        return memo[x][y]

    t = arr[x][y]
    memo[x][y] = max(get_max(x - 1, y, t), get_max(x + 1, y, t), get_max(x, y - 1, t), get_max(x, y + 1, t)) + 1

    return memo[x][y]

for i in range(n):
    for j in range(n):
        visited[i][j] = True
        get_max(i, j, arr[i][j])

print(memo)