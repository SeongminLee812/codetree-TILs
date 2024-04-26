n, m = map(int, input().split())

pelindromes = 0

for i in range(n, m + 1):
    strings = list(str(i))
    if strings == strings[::-1]:
        pelindromes += 1
print(pelindromes)