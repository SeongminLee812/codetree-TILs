from itertools import combinations
from copy import deepcopy
from collections import deque

# input
n, k, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
start_point = []
for _ in range(k):
    r, c = map(int, input().split())
    start_point.append((r - 1, c - 1))

# stone`s position
stones_pos = []
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            stones_pos.append((i, j))

# remove candidate of stone
rm_candidate = combinations(stones_pos, m)

def remove_stone(matrix, x, y):
    """
    remove stone from raw matrix
    :param matrix: raw matrix
    :param x: row of stone
    :param y: column of stone
    :return: None
    """
    matrix[x][y] = 0
    return matrix

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(matrix, x, y):
    if not in_range(x, y):
        return False
    if matrix[x][y] == 1 or visited[x][y]:
        return False
    return True

def bfs(matrix):
    global q, total
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        total += 1
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(matrix, nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))


ans = 0

for stones in rm_candidate:
    matrix = deepcopy(a)
    # visited 초기화
    visited = [[False] * n for _ in range(n)]
    for stone_x, stone_y in stones:
        ## 돌 치우기
        matrix = remove_stone(matrix, stone_x, stone_y)

    print(matrix)
    # 전체 배열 순회하면서
    for i in range(n):
        for j in range(n):
            total = 0
            q = deque()
            if not visited[i][j] and matrix[i][j] == 0:
                visited[i][j] = True
                q.append((i, j))
                # bfs 수행
                bfs(matrix)
                # 방문 가능한 최대 수
                ans = max(ans, total)

print(ans)