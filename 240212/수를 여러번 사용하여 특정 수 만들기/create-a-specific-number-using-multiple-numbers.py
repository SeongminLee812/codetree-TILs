a, b, c = map(int, input().split())

max_val = 0

for i in range(0, c // a + 1):
    a_val = a * i

    remain = c - a_val

    num_b = remain // b
    b_val = num_b * b

    now_value = a_val + b_val
    max_val = max(now_value, max_val)

print(max_val)