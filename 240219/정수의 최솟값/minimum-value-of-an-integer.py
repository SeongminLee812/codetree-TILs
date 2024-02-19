def min_3(*args):
    return min(args)

a, b, c = map(int, input().split())
print(min_3(a, b, c))