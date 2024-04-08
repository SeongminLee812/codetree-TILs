import sys
import heapq
INT_MIN = -sys.maxsize
sys.setrecursionlimit(10)

n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

memo = [
    [0] * n
    for _ in range(n)
]

visited = [
    [False] * n
    for _ in range(n)
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n



def can_go(x, y, t):
    if not in_range(x, y):
        return False
    if memo[x][y]:
        return False
    if arr[x][y] <= t:
        return False
    return True

def get_max(x, y, threshold, step):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny, threshold):
            memo[nx][ny] = step + 1
            get_max(nx, ny, arr[nx][ny], step + 1)


    return memo[x][y]

# 우선순위 힙
q = []
for i in range(n):
    for j in range(n):
        heapq.heappush(q, (arr[i][j], i, j))

for value, i, j in q:
    if not memo[i][j]:
        memo[i][j] = 1
        get_max(i, j, value, 1)

ans = 0
for line in memo:
    ans = max(ans, max(line))

print(ans)