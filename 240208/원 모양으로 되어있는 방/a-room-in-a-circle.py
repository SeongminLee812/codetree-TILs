import sys

n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

ans = sys.maxsize

for i in range(n):
    new_list = a[i:] + a[:i]
    distance = 0
    for j in range(n):
        distance += j * new_list[j]
    ans = min(ans, distance)

print(ans)