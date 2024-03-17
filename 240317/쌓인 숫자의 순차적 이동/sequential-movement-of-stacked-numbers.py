n, m = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
for i in range(n):
    for j in range(n):
        arr[i][j] = [arr[i][j]]

print(arr)
directions = list(map(int, input().split()))

def search(num):
    for i in range(n):
        for j in range(n):
            if num in arr[i][j]:
                return i, j

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def move(num):
    dxs = [-1, -1, -1, 0, 1, 1, 1, 0]
    dys = [-1, 0, 1, 1, 1, 0, -1, -1]

    x, y = search(num)
    max_pos = 0, 0
    max_val = 0

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and arr[nx][ny]:
            for val in arr[nx][ny]:
                if val > max_val:
                    max_val = val
                    max_pos = nx, ny

    next_x, next_y = max_pos

    key = arr[x][y]
    key_index = key.index(num)
    seg = key[key_index:]
    # 해당 숫자 위에 있는 숫자 전부 제거
    arr[x][y][key_index:] = []
    # 이동
    arr[next_x][next_y] += seg

for d in directions:
    move(d)

for i in range(n):
    for j in range(n):
        if not arr[i][j]:
            print(None)
        else:
            print(' '.join(map(str, arr[i][j][::-1])))