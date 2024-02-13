# 최대값을 정해 최대값을 피해서 도달할 수 있는 지 탐색

n, k = map(int, input().split())
arr = list(map(int, input().split()))

def is_possible(max_val):
    available_indices = []
    for i, elem in enumerate(arr):
        if elem <= max_val:
            available_indices.append(i)

    arr_size = len(available_indices)
    for i in range(1, arr_size):
        dist = available_indices[i] - available_indices[i - 1]
        if dist > k:
            return False

    return True

ans = n

for i in range(n, 1, -1):
    if is_possible(i):
        ans = i

print(ans)