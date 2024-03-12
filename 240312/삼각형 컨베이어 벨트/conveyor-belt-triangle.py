n, t = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(3)
]

for _ in range(t):
    temp = arr[2][n - 1]

    for i in range(n * 3 - 1, 0, -1):
        arr[i // 3][i % 3] = arr[(i - 1) // 3][(i - 1) % 3]

    arr[0][0] = temp

for line in arr:
    print(' '.join(map(str, line)))