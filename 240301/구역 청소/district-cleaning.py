a, b = map(int, input().split())
c, d = map(int, input().split())

def intersecting():
    if a > d or b < c:
        return False
    return True

if intersection():
    ans = max([b, d]) - min([a, ])
else:
    ans = (b - a) + (d - c)

print(ans)