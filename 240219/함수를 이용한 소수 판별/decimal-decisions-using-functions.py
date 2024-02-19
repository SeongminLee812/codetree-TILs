primes = [True] * 101
primes[0] = False
primes[1] = False

for i in range(2, 101 // 2):
    num = i + i
    while num <= 100:
        primes[num] = False
        num += i

def is_prime(num):
    return primes[num]

def how_many_prime(a, b):
    total = 0
    for i in range(a, b + 1):
        if is_prime(i):
            total += i
    return total

a, b = map(int, input().split())

print(how_many_prime(a, b))