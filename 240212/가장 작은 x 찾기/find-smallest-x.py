n = int(input())
ab_list = []
for _ in range(n):
    a, b = map(int, input().split())
    ab_list.append((a, b))

for x in range(1, 10001):
    first_x = x
    ok = True
    x *= 2
    for a, b in ab_list:
        if x > b or x < a:
            ok = False
            break
        x *= 2
    if ok:
        print(first_x)
        break