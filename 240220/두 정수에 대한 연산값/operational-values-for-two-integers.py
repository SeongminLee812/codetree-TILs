def modify(a, b):
    if a > b:
        a += 25
        b *= 2
    else:
        a *= 2
        b += 25
    return a, b

a, b= map(int, input().split())

a, b = modify(a, b)
print(a, b)