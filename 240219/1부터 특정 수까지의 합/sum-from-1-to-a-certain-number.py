def sum_div(n):
    total = sum(i for i in range(1, n + 1))
    total //= 10
    return total

n = int(input())
print(sum_div(n))