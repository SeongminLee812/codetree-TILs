def is_onjeon(num):
    if num % 2 == 0:
        return False
    if num % 10 == 5:
        return False
    if num % 3 == 0 and num % 9 != 0:
        return False
    return True

a, b = map(int, input().split())

ans = 0
for i in range(a, b + 1):
    if is_onjeon(i):
        ans += 1

print(ans)