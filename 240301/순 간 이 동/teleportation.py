a, b, x, y = map(int, input().split())

# a -> x -> y -> b
first = abs(a - x) + abs(y - b)

# a -> y -> x -> b
second = abs(a - y) + abs(b - x)

# a -> b
third = abs(b - a)

ans = min([first, second, third])
print(ans)