n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False] * n
    for _ in range(n)
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or arr[x][y] == 0:
        return False
    return True

def dfs(x, y):
    global humans
    dxs = [0, 0, -1, 1]
    dys = [-1, 1, 0, 0]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            visited[nx][ny] = True
            humans += 1
            dfs(nx, ny)


village = 0
humans_list = []

for i in range(n):
    for j in range(n):
        if can_go(i, j):
            visited[i][j] = True
            village += 1
            humans = 1
            dfs(i, j)
            humans_list.append(humans)

print(village)
for h in sorted(humans_list):
    print(h)