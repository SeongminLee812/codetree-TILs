import heapq

n, B = map(int, input().split())

p = []
s = []
totals = []

for _ in range(n):
    a, b = map(int, input().split())
    p.append(a)
    s.append(b)
    totals.append(a + b)

# 합계값을 기준으로 정렬 및 인덱스 뽑기
q = []
result_p = []
result_s = []

for index, value in enumerate(totals):
    heapq.heappush(q, (value, index))

for _ in range(len(q)):
    value, index = heapq.heappop(q)
    result_p += [p[index]]
    result_s += [s[index]]

ans = 0
for i in range(n):
    result_p[i] //= 2
    buyable_count = 0
    money = B
    for j in range(n):
        receipt = result_p[j] + result_s[j]
        money -= receipt
        buyable_count += 1
        if money < 0:
            buyable_count -= 1
            break
    ans = max(ans, buyable_count)
    result_p[i] *= 2

print(ans)