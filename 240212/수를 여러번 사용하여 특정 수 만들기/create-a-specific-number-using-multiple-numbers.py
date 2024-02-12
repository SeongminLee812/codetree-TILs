a, b, c = map(int, input().split())

max_val = 0

for i in range(0, 1001):
    if a * i > c:
        break
    for j in range(0, 1001):
        now_val = a * i + b * j
        if now_val > c:
            break
        max_val = max(now_val, max_val)

print(max_val)