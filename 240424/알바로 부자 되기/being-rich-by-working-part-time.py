n = int(input())

albas = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

# 끝나는 시간 기준으로 오름차순 정렬
albas.sort(key=lambda x: x[1])

albas = [0] + albas
s = [0] * (n + 1)
e = [0] * (n + 1)
p = [0] * (n + 1)

for i in range(1, n + 1):
    s[i], e[i], p[i] = albas[i]

dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(i):
        if e[j] < s[i]:
            dp[i] = max(dp[i], dp[j] + p[i])

print(max(dp))