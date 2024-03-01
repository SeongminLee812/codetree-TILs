n = int(input())

pigeons = [
    []
    for _ in range(10 + 1)
]

for _ in range(n):
    p, road = map(int, input().split())
    pigeons[p].append(road)

cnt = 0
for i in range(n):
    if len(pigeons[i]) >= 2:
        for j in range(len(pigeons[i]) - 1):
            if pigeons[i][j] != pigeons[i][j + 1]:
                cnt += 1
print(cnt)