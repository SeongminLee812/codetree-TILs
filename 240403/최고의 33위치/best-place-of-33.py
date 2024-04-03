n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def count_coin(start_x, start_y):
    cnt = 0
    for i in range(start_x, start_x + 3):
        for j in range(start_y, start_y + 3):
            if arr[i][j] == 1:
                cnt += 1
    return cnt


ans = 0

for i in range(n - 2):
    for j in range(n - 2):
        ans = max(ans, count_coin(i, j))

print(ans)