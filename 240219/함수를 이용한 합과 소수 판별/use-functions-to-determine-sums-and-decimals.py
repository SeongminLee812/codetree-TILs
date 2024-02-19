primes = [True] * 101
primes[0] = primes[1] = False

for i in range(2, 100 // 2 + 1):
    num = i + i
    while num <= 100:
        primes[num] = False
        num += i

def is_magic(num):
    all_num_total = 0
    while num:
        all_num_total += num % 10
        num //= 10
    return all_num_total % 2 == 0

def is_prime(num):
    return primes[num]

a, b = map(int, input().split())
ans = 0
for i in range(a, b + 1):
    if is_magic(i) and is_prime(i):
        ans += 1

print(ans)