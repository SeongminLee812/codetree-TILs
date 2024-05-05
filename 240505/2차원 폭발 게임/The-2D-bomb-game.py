import copy

n, m, k = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def search_and_boom(x, y):
    start_row = x
    row = x
    count = 1
    while row < n - 1 and arr[row][y] == arr[row + 1][y]:
        count += 1
        row += 1
    final_row = row
    if count >= m:
        for row in range(start_row, final_row + 1):
            arr[row][y] = 0

def rotate(original_array):
    new_arr = [
        [0] * n
        for _ in range(n)
    ]
    for i in range(n):
        for j in range(n):
            new_arr[i][j] = original_array[n - j - 1][i]

    return new_arr

def pull_gravity(original_array):
    new_arr = [
        [0] * n
        for _ in range(n)
    ]

    for col in range(n):
        temp_arr = [0] * n
        temp_index = n - 1
        for row in range(n - 1, -1, -1):
            if original_array[row][col]:
                new_arr[temp_index][col] = original_array[row][col]
                temp_index -= 1

    return new_arr

for _ in range(k):
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                search_and_boom(i, j)

    gravity_array = pull_gravity(arr)
    rotate_array = rotate(gravity_array)
    gravity_array = pull_gravity(rotate_array)
    arr = copy.deepcopy(gravity_array)

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            search_and_boom(i, j)

ans = 0
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            ans += 1
print(ans)