n, m = map(int, input().split())

# 최대 공약수
def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

def lcd(x, y):
    return x * y // gcd(x, y)

print(lcd(n, m))