def total(n):
    if n == 1:
        return 1
    return total(n - 1) + n

n = int(input())
print(total(n))