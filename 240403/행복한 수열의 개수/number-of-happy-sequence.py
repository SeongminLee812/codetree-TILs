n, m = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def is_happy(num_array):
    cnt = 1
    if len(num_array) == 1:
        return True
    for i in range(n - 1):
        if num_array[i] == num_array[i + 1]:
            cnt += 1
        else:
            cnt = 1
        if cnt >= m:
            return True
    return False

ans = 0
for i in range(n):
    row = [arr[i][j] for j in range(n)]
    col = [arr[j][i] for j in range(n)]
    if is_happy(row):
        ans += 1
    if is_happy(col):
        ans += 1

print(ans)