def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

def lcm(x, y):
    return (x * y) // gcd(x, y)

n, m = map(int, input().split())

print(lcm(n, m))