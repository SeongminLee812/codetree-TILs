n = int(input())

arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

def overlap(segment1, segment2):
    x1, x2 = segment1
    y1, y2 = segment2
    if x2 < y1 or x1 > y2:
        return False
    return True

all_okay = False

for i in range(n):
    check_arr = arr[:i] + arr[i + 1:]
    is_okay = True
    for j in range(n - 1):
        for k in range(j + 1, n - 1):
            if not overlap(check_arr[j], check_arr[k]):
                is_okay = False
                break
        if not is_okay:
            break

    if is_okay:
        all_okay = True
        break

if  n == 1 or all_okay:
    print('Yes')
else:
    print('No')