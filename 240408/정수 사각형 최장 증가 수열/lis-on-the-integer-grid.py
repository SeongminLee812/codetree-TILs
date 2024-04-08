import heapq

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

def can_go(x, y, t):
    if not in_range(x, y):
        return False
    if visited[x][y]:
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
        if can_go(nx, ny, arr[x][y]):
            heapq.heappush(_heap, (arr[nx][ny], nx, ny))

    # print('now :', x, y,)
    # print(_heap)
    for _, nx, ny in _heap:
        memo[nx][ny] = step + 1
        visited[nx][ny] = True
        get_max(nx, ny, step + 1)

    return memo[x][y]


# 우선순위 힙
q = []
for i in range(n):
    for j in range(n):
        heapq.heappush(q, (arr[i][j], i, j))

for _, i, j in q:
    if not visited[i][j]:
        visited[i][j] = True
        memo[i][j] = 1
        get_max(i, j, 1)

ans = 0
for line in memo:
    # print(line)
    ans = max(ans, max(line))

print(ans)

### 테스트 케이스
"""
10 
7 2 7 7 17 1 8 5 6 7
7 3 4 57 87 4 2 6 8 12
7 6 5 5 7 9 15 45 2 6
1 2 3 4 5 4 7 5 6 2 
11 51 65 8 1 21 45 4 6 8
1 2 2 4 5 8 41 3 1 2 7
12 15 4 1 2 51 6 8 4 6 
1 25 35 41 51 55 56 57 58 59
12 53 51 59 57 58 60 61 62 63
18 6 4 1 5 8 67 81 98 99
"""