a, b = map(int, input().split())

if a > b:
    a *= 2
    b += 10
else:
    a += 10
    b *= 2

print(a, b)