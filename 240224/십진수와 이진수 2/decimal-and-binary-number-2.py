binary = list(map(int, (list(input()))))

num = 0
for i in range(len(binary)):
    num = num * 2 + binary[i]

num *= 17

digits = []
while True:
    if num < 2:
        digits.append(num)
        break
    digits.append(num % 2)
    num //= 2

print(''.join(map(str, digits[::-1])))