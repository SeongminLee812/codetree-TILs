n = int(input())
segments = []
for _ in range(n):
    a, b = map(int, input().split())
    segments.append((a, b))

ok = False

for i in range(n):
    if i == 0:
        now_seg = segments[i + 1:]
    elif i == n - 1:
        now_seg = segments[:i]
    else:
        now_seg = segments[:i] + segments[i + 1:]

    max_a = max(now_seg, key=lambda x: x[0])[0]
    min_b = min(now_seg, key=lambda x: x[1])[1]

    if min_b >= max_a:
        print('Yes')
        ok = True
        break

if not ok:
    print('No')