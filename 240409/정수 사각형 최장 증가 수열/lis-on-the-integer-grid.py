import heapq
import sys
sys.setrecursionlimit(250001)

# with open('input.txt', 'r') as f:
#     n = int(f.readline())
#
#     arr = [
#         list(map(int, f.readline().split()))
#         for _ in range(n)
#     ]


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

def can_go(x, y, t, step):
    if not in_range(x, y):
        return False
    if memo[x][y] >= step:
        return False

    if arr[x][y] <= t:
        return False
    return True

def get_max(x, y, step):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    _heap = []
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        # 오른차순 정렬 필요 -> 작은 수 부터 방문
        if can_go(nx, ny, arr[x][y], step):
            heapq.heappush(_heap, (arr[nx][ny], nx, ny)) # 이때 이미 넣어놈

    # print('now :', x, y,)
    # print(_heap)
    for _, nx, ny in _heap:
        if memo[nx][ny] < step:
            memo[nx][ny] = step
        get_max(nx, ny, step + 1)

    return memo[x][y]


# 우선순위 힙
q = []
for i in range(n):
    for j in range(n):
        heapq.heappush(q, (arr[i][j], i, j))

for _, i, j in q:
    if memo[i][j] == 0:
        memo[i][j] = 1
        get_max(i, j, 2)

ans = 0
for line in memo:
    ans = max(ans, max(line))

print(ans)