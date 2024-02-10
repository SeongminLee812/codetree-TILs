n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def second_search(x, y):
    res = 0 # search max value
    cnt = 0

    for j in range(y + 3, n - 2): # search same row
        if j + 2 >= n:
            break
        cnt = arr[x][j] + arr[x][j + 1] + arr[x][j + 2]

    res = max(res, cnt)

    cnt = 0
    for i in range(x + 1, n):
        if x + 1 >= n:
            break
        for j in range(0, n - 2):
            cnt = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
            res = max(res, cnt)
    return res

ans = 0
for i in range(n):
    for j in range(0, n - 2):
        cnt = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
        cnt += second_search(i, j)
        ans = max(ans, cnt)

print(ans)