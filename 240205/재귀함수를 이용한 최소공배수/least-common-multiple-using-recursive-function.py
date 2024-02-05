def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

def lcm(x, y):
    return (x * y) // gcd(x, y)

def get_all_lcm(n):
    if n == 0:
        return a[n]

    return lcm(a[n], get_all_lcm(n - 1))

n = int(input())
a = list(map(int, input().split()))

print(get_all_lcm(n - 1))