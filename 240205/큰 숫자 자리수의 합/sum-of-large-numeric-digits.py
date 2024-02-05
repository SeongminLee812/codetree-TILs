nums = map(int, input().split())
n = 1
for i in nums:
    n *= i

def f(n):
    if n < 10:
        return n
    return f(n // 10) + f(n % 10)

print(f(n))