arr = list(map(int, input().split()))

def is_equal(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for a, b in zip(arr1, arr2):
        if a != b:
            return False

    return True

for a in range(1, 41):
    for b in range(a, 41):
        for c in range(b, 41):
            for d in range(c, 41):
                if is_equal([a, b, c, d, a + b, b + c, c + d,
                          d + a, a + c, b + d, a + b + c,
                          a + b + d, a + c + d, b + c + d,
                          a + b + c + d], arr):
                    print(a, b, c, d)