n = int(input())

pigeons = [
    []
    for _ in range(10 + 1)
]

for _ in range(n):
    p, road = map(int, input().split())
    pigeons[p].append(road)

cnt = 0
for i in range(11):
    pigeon = pigeons[i]
    if len(pigeon) >= 2:
        for j in range(len(pigeon) - 1):
            if pigeon[j] != pigeon[j + 1]:
                cnt += 1

print(cnt)