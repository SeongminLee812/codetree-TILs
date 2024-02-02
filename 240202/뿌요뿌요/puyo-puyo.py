n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y, value):
    if not in_range(x, y):
        return False

    if visited[x][y] or a[x][y] != value:
        return False

    return True

# dfs
def dfs(x, y, value):
    global block_num
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if can_go(nx, ny, value):
            block_num += 1 # block 개수 체크
            visited[nx][ny] = True
            dfs(nx, ny, value)

bomb_num = 0

max_block = 0

for i in range(n):
    for j in range(n):
        block_num = 1
        if not visited[i][j]:
            visited[i][j] = True
            value = a[i][j] # 값 넘기기
            dfs(i, j, value)
            max_block = max(max_block, block_num)
            if block_num >= 4:
                bomb_num += 1

print(bomb_num, max_block)