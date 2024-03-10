n, t = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(2)
]

# 두번째 줄 뒤집기
new_arr = [0] * n
for i in range(n):
    new_arr[i] = arr[1][n - 1 - i]
arr[1] = new_arr

for _ in range(t):

    # 첫번째 행은 밀어주기
    first_row_key = arr[0][n - 1]

    for i in range(n - 1, 0, -1):
        arr[0][i] = arr[0][i - 1]

    # 두번째 행은 당겨주기
    second_row_key = arr[1][0]

    for j in range(n - 1):
        arr[1][j] = arr[1][j + 1]

    # 빈자리 매꿔주기
    arr[1][n - 1] = first_row_key
    arr[0][0] = second_row_key

# 두번째 줄 뒤집기
new_arr = [0] * n
for i in range(n):
    new_arr[i] = arr[1][n - 1 - i]
arr[1] = new_arr

for line in arr:
    print(' '.join(map(str, line)))