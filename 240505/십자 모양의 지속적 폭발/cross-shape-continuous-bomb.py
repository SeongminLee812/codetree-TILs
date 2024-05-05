n, m = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
columns = [int(input()) - 1 for _ in range(m)]

# 함수 구현
# 1. in_range(x, y),
# 2. pull_gravity() : 중력 작용을 통해 위에 있는 숫자를 아래로 당김
# 3. boom(x, y) : 해당 위치에서 폭발이 시작되어 폭발 작용
# 4. select_bomb(y) : 어떤 폭탄을 고를 지 선택, 열의 위치가 주어지면 위에서부터 탐색하여 처음 0이 아닌 폭탄 선택함

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def pull_gravity():
    for col in range(n):
        new_array = [0] * n
        new_index = n - 1
        for row in range(n - 1, -1, -1):
            if arr[row][col]:
                new_array[new_index] = arr[row][col]
                new_index -= 1
        for row in range(n):
            arr[row][col] = new_array[row]

def boom(x, y):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    boom_range = arr[x][y]
    arr[x][y] = 0

    for step in range(1, boom_range):
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx * step, y + dy * step
            if in_range(nx, ny):
                arr[nx][ny] = 0

def select_boom(column):
    for row in range(n):
        if arr[row][column]:
            return row, column
    return False

for col in columns:
    target = select_boom(col)
    if target:
        x, y = target
        boom(x, y)
        pull_gravity()

for line in arr:
    print(' '.join(map(str, line)))