n, k = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
for i in range(0, n - k + 1):
    val = 0
    for j in range(i, i + k):
        val += arr[j]

    ans = max(ans, val)

print(ans)