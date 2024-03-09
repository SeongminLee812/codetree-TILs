import sys

n = int(input())

x1_list = []
x2_list = []
for _ in range(n):
    x1, x2 = map(int, input().split())
    x1_list.append(x1)
    x2_list.append(x2)

ans = sys.maxsize

for skip in range(n):
    max_x2 = 0
    min_x1 = sys.maxsize

    for i in range(n):
        if i == skip:
            continue

        max_x2 = max(max_x2, x2_list[i])
        min_x1 = min(min_x1, x1_list[i])

    length = max_x2 - min_x1
    ans = min(ans, length)

print(ans)