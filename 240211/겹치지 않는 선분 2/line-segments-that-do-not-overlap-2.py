n = int(input())
lines = []
for _ in range(n):
    x1, x2 = map(int, input().split())
    # x1, x2 = x1 + 1000000, x2 + 1000000
    lines.append((x1, x2))

def check(first, second):
    if first[0] <= second[0] and second[1] <= second[0]:
        return False
    if second[0] <= first[0] and first[1] <= second[1]:
        return False
    return True

ans = 0
for i in range(n):
    ok = True
    for j in range(n):
        if i == j:
            continue
        if not check(lines[i], lines[j]):
            ok = False
    if ok:
        ans += 1

print(ans)