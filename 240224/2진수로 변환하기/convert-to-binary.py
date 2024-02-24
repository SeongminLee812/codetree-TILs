n = int(input())

digits = []

while True:
    if n < 2:
        digits.append(n)
        break
    
    digits.append(n % 2)
    n //= 2

print(''.join(map(str, digits[::-1])))