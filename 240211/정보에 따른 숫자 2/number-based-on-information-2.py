t, a, b = map(int, input().split())

placed = [0] * 1001

for _ in range(t):
    alpha, place = input().split()
    place = int(place)
    placed[place] = alpha

MAX_INT = 1001

ans = 0
for x in range(a, b + 1):
    min_s = MAX_INT
    min_n = MAX_INT
    for i in range(0, 1001):
        if placed[i] == 'S':
            diff = abs(x - i)
            min_s = min(min_s, diff)
        if placed[i] == 'N':
            diff = abs(x - i)
            min_n = min(min_n, diff)
    if min_s <= min_n:
        ans += 1
print(ans)