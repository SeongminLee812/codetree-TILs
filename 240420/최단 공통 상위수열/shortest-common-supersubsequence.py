# 풀이 : a길이 + b길이 - lcs 길이
# 이해 : a와 b의 합집합 원소의 개수는, 각 집합의 원소의 개수를 더한 후, 교집합의 원소의 개수를 뺀다.
a = " " + input()
b = " " + input()

dp = [
    [0] * len(b)
    for _ in range(len(a))
]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(len(a) - 1 + len(b) - 1 - dp[len(a) - 1][len(b) - 1])