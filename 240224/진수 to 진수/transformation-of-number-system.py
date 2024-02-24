a, b = map(int, input().split())
n = int(input())

# n을 십진수로 변환
num = 0
binary = list(map(int, list(str(n))))

for i in range(len(binary)):
    num = num * a + binary[i]

# num을 b진수로 변환
digits = []
while True:
    if num < b:
        digits.append(num)
        break

    digits.append(num % b)
    num //= b

print(''.join(map(str, digits[::-1])))