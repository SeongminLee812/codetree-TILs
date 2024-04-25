def calc(a, b):
    if a > b:
        return a * 2, b + 10
    else:
        return a + 10, b * 2
    
a, b = map(int, input().split())
print(*calc(a, b))