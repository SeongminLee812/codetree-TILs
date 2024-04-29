import sys

n = int(input())

segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

ans = sys.maxsize

for i in range(n):
    min_x1, max_x2 = sys.maxsize, 0
    for j in range(n):
        if i == j:
            continue
        min_x1 = min(min_x1, segments[j][0])
        max_x2 = max(max_x2, segments[j][1])
    ans = min(ans, max_x2 - min_x1)

print(ans)