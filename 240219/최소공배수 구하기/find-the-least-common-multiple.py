n, m = map(int, input().split())

def lcm(n, m):
    result = -1
    for i in range(1, 101):
        if i % n == 0 and i % m == 0:
            result = i
            return result
    return result

print(lcm(n, m))