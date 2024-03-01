import copy

n, b = map(int, input().split())

prices = []
ships = []

for _ in range(n):
    p, s = map(int, input().split())
    prices.append(p)
    ships.append(s)

ans = 0

# n개중 하나만 반값.
# 정렬 -> 싼 애들부터 채우면 됨
for i in range(n):
    now_p = copy.deepcopy(prices)
    now_p[i] //= 2
    remain_cost = b
    student = 0

    now_p.sort()
    for j in range(n):
        remain_cost -= now_p[j]
        if remain_cost > 0:
            student += 1
        else:
            break
    ans = max(ans, student)

print(ans)