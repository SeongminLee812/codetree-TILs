a, b = map(int, input().split())
c, d = map(int, input().split())

def intersecting():
    if a > d or b < c:
        return False
    return True

if intersecting():
    ans = max([b, d]) - min([a, c])
else:
    ans = (b - a) + (d - c)

print(ans)