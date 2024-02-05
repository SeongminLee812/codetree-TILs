total = 0
def f(n):
    global total
    if n == 1:
        return
    total += 1
    if n % 2 == 0:
        return f(n // 2)
    else:
        return f(n * 3 + 1)

n = int(input())
f(n)
print(total)