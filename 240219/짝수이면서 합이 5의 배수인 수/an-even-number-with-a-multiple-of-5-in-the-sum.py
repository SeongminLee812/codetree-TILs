def is_five_mul(num):
    total = 0
    while num:
        total += num % 10
        num //= 10
    return total % 5 == 0

def is_magic_num(num):
    if num % 2 == 0 and is_five_mul(num):
        print('Yes')
    else:
        print('No')

n = int(input())
is_magic_num(n)