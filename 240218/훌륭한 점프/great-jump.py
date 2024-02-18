n, k = map(int, input().split())
arr = list(map(int, input().split()))

def check_distance(limit):
    cango_indices = [i for i in range(n) if arr[i] <= limit]

    # print(f'limit={limit}, cango_indices={cango_indices}')
    prev_i = 0
    for i in range(len(cango_indices)):
        if cango_indices[i] - cango_indices[prev_i] > k:
            return False
        prev_i = i

    return True


ans = 0
for limit in range(max(arr[0], arr[-1]), max(arr) + 1):
    if check_distance(limit):
        ans = limit
        break

print(ans)