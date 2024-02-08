n = int(input())
a = [list(map(int, input().split())) 
        for _ in range(n)]

ans = 0
for i in range(n):
        for j in range(n - 2):
                ans = max(ans, a[i][j] + a[i][j + 1] + a[i][j + 2])

print(ans)