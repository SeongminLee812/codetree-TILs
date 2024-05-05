import copy

n, m, k = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def search_condition(x, y):
    start_row = x
    row = x
    count = 1
    while row < n - 1 and arr[row][y] == arr[row + 1][y]:
        count += 1
        row += 1
    final_row = row

    if count >= m:
        return start_row, final_row

    return False

def boom_from_to(start_row, final_row, col):
    for row in range(start_row, final_row + 1):
        arr[row][col] = 0

def boom():
    for i in range(n):
        for j in range(n):
            target = search_condition(i, j)
            if target:
                start_row, final_row = target
                boom_from_to(start_row, final_row, j)

def rotate():
    new_arr = [
        [0] * n
        for _ in range(n)
    ]
    for i in range(n):
        for j in range(n):
            new_arr[i][j] = arr[n - j - 1][i]

    for i in range(n):
        for j in range(n):
            arr[i][j] = new_arr[i][j]

def pull_gravity():
    new_arr = [
        [0] * n
        for _ in range(n)
    ]

    for col in range(n):
        temp_arr = [0] * n
        temp_index = n - 1
        for row in range(n - 1, -1, -1):
            if arr[row][col]:
                new_arr[temp_index][col] = arr[row][col]
                temp_index -= 1

    for i in range(n):
        for j in range(n):
            arr[i][j] = new_arr[i][j]


def all_search():
    visited = [
        [False] * n
        for _ in range(n)
    ]
    for i in range(n):
        for j in range(n):
            if arr[i][j] and not visited[i][j]:
                if search_condition(i, j):
                    return True
    return False

for _ in range(k):
    while all_search():
        boom()
        # 여기서 터질 게 있으면 계속 터뜨리도록
        pull_gravity()

    rotate()
    pull_gravity()

while all_search():
    boom()
    pull_gravity()


ans = 0
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            ans += 1
print(ans)