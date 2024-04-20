n, m = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def all_positive(start_x, start_y, end_x, end_y):
    all_pos = True
    for i in range(end_x, start_x - 1, -1):
        for j in range(end_y, start_y - 1, -1):
            if arr[i][j] < 0:
                return False
    return all_pos


max_rec = 0
for i in range(n):
    for j in range(m):
        for nx in range(n - 1, i - 1, -1):
            for ny in range(m - 1, j - 1, -1):
                if all_positive(i, j, nx, ny):
                    max_rec = max(max_rec, (nx - i + 1) * (ny - j + 1))

print(max_rec)