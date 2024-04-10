n, m = map(int, input().split())
coins = list(map(int, input().split()))

memo = [10001] * (10001)
for j in range(n):
    memo[coins[j]] = 1

memo[0] = 1

# memoization 풀이
def memoization(index):
    if memo[index] < 10001:
        return memo[index]

    best = 10001
    for j in range(n):
        if index >= coins[j]:
            best = min(best, memoization(index - coins[j]) + 1)
    memo[index] = best
    return memo[index]

ans = memoization(m)
if ans < 10001:
    print(ans)
else:
    print(-1)