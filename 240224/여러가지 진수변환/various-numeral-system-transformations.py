n, b = map(int, input().split())
digits = []

while True:
    if n < b:
        digits.append(n)
        break
    digits.append(n % b)
    n //= b

print(''.join(map(str, digits[::-1])))