def pos_exp(n):
    if n < 10:
        return n ** 2
    return pos_exp(n // 10) + ((n % 10) ** 2)

n = int(input())
print(pos_exp(n))