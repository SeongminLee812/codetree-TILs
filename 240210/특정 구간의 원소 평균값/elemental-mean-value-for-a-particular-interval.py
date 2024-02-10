n = int(input())
arr = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i, n):
        total = sum(arr[i:j + 1])
        share, remainder = divmod(total, j - i + 1)
        if remainder:
            continue
        if share in arr[i:j + 1]:
            ans += 1

print(ans)