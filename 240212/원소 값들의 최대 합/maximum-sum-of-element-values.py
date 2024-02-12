n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr = [0] + arr

ans = 0

for i in range(1, n + 1):
    val = 0
    pos = i
    for _ in range(m):
        val += arr[pos]
        pos = arr[pos]
    ans = max(ans, val)

print(ans)