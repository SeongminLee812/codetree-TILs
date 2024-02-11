from collections import defaultdict

x, y = map(int, input().split())

def check(num):
    array = [0] * 10

    while num:
        digit = num % 10
        num // 10
        array[digit] += 1

    for i in range(10):
        if array[i] == sum(array) - 1:
            return True

    return False

ans = 0
for i in range(x, y + 1):
    if check(i):
        ans += 1

print(ans)