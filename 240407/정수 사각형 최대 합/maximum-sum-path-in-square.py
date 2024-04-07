n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

# initialize
memo = [
    [-1] * n
    for _ in range(n)
]

memo[0][0] = arr[0][0]

for i in range(1, n):
    memo[i][0] = memo[i - 1][0] + arr[i][0]
    memo[0][i] = memo[0][i - 1] + arr[0][i]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def get_sum(x, y):
    if not in_range(x, y):
        return
    if memo[x][y] != -1:
        return memo[x][y]
    else:
        memo[x][y] = max(get_sum(x - 1, y), get_sum(x, y - 1)) + arr[x][y]
    return memo[x][y]

get_sum(n - 1, n - 1)
print(memo[n - 1][n - 1])