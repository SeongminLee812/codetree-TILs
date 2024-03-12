n, t = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(3)
]

for _ in range(t):
    temp = arr[2][n - 1]

    for i in range(n * 3 - 1, 0, -1):
        try:
            arr[i // n][i % n] = arr[(i - 1) // n][(i - 1) % n]
        except:
            print(i)
            raise IndexError

    arr[0][0] = temp

for line in arr:
    print(' '.join(map(str, line)))