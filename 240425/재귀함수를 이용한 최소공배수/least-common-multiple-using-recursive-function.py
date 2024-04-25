n = int(input())
arr = list(map(int, input().split()))

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

def lcd(x, y):
    return x * y // gcd(x, y)


def get_ans(n):
    if n == 0:
        return arr[n]
    return lcd(arr[n], get_ans(n - 1))

print(get_ans(n - 1))