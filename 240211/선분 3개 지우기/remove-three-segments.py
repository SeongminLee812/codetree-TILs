import copy

n = int(input())

lines = []
placed = [0] * 101
for _ in range(n):
    a, b = map(int, input().split())
    lines.append((a, b))
    for x in range(a, b + 1):
        placed[x] += 1

def check(i, j, k):
    check_line = copy.deepcopy(placed)
    a1, b1 = lines[i]
    a2, b2 = lines[j]
    a3, b3 = lines[k]

    for a, b in zip([a1, a2, a3], [b1, b2, b3]):
        for x in range(a, b + 1):
            check_line[x] -= 1

    for x in range(0, 101):
        if check_line[x] >= 2:
            return False
    return True

ans = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if check(i, j, k):
                ans += 1

print(ans)