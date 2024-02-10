n = int(input())

working = []
for _ in range(n):
    a, b = map(int, input().split())
    working.append((a, b))

ans = 0
for i in range(n):
    times = [0] * 1000
    for j in range(n):
        if i == j:
            continue
        start, end = working[j]
        times[start:end] = [1] * (end - start)
    total = sum(times)
    ans = max(ans, total)

print(ans)