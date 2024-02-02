import copy

# input
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m


def can_go(x, y):
    if not in_range(x, y):
        return False

    if visited[x][y]:
        return False

    if curr_a[x][y] == 0:
        return False
    return True


def dfs(x, y):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if can_go(nx, ny):
            visited[nx][ny] = True
            dfs(nx, ny)


def search(matrix):
    adjacency_cnt = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                adjacency_cnt += 1

    return adjacency_cnt

max_k = 0
for line in a:
    max_k = max(max_k, max(line))

ans_cnt, ans_k = 0, 1

for k in range(1, max_k + 1):
    curr_a = copy.deepcopy(a)
    for i in range(n):
        for j in range(m):
            if curr_a[i][j] > k:
                curr_a[i][j] = 1
            else:
                curr_a[i][j] = 0

    visited = [[False] * m for _ in range(n)]
    cnt = search(curr_a)
    if ans_cnt < cnt:
        ans_cnt = cnt
        ans_k = k

print(ans_k, ans_cnt)