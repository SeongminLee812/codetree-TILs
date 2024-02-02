n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y):
    return in_range(x, y) and a[x][y] == 1 and visited[x][y] == False

def dfs(x, y):
    global human
    # print(f'pos={x}, {y}\tvilleges={villedges} \t human={human}')
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            visited[nx][ny] = True
            human += 1
            dfs(nx, ny)

humans = []
call_num = 0

villedges = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and not visited[i][j]:
            human = 1
            visited[i][j] = True
            dfs(i, j)
            villedges += 1
            humans.append(human)

humans.sort()
print(villedges)
print('\n'.join(map(str, humans)))