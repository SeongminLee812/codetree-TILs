n, s = map(int, input().split())
arr = list(map(int, input().split()))

ans = s
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        value = sum(arr) - arr[i] - arr[j]
        diff = abs(s - value)
        ans = min(ans, diff)

print(ans)