n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(min(i + 1, n), n):
        for k in range(min(j + 1, n), n):
            if a[i] <= a[j] <= a[k]:
                ans += 1

print(ans)