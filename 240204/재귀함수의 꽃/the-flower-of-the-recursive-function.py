def print_num(n):
    if n == 0:
        return
    print(n, end=' ')
    print_num(n - 1)
    print(n, end=' ')

n = int(input())
print_num(n)