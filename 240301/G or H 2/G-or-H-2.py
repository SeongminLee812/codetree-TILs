# search starting point i
# search district range j

n = int(input())
arr = [0] * (100 + 1)

max_position = 0

for _ in range(n):
    pos, alpha = input().split()
    pos = int(pos)
    arr[pos] = alpha
    max_position = max(max_position, pos)

ans = 0

for i in range(max_position + 1):
    for j in range(1, max_position + 1 - i):
        g_count = 0
        h_count = 0
        district = arr[i: i + j + 1]
        if district[0] == 0 or district[-1] == 0:
            continue
        for d in district:
            if d == 'G':
                g_count += 1
            elif d == 'H':
                h_count += 1
        if (g_count == h_count):
            ans = max(ans, j)
        if not h_count:
            ans = max(ans, j)
        if not g_count:
            ans = max(ans, j)

print(ans)