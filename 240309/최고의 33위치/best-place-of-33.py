n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def count_coin(start_row, start_col):
    count = 0
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if arr[i][j]:
                count += 1

    return count

ans = 0

for row in range(n - 2):
    for col in range(n - 2):
        cnt = count_coin(row, col)
        ans = max(cnt, ans)

print(ans)