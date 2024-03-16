n, m, k = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def check_next_row(curr_row):
    next_row = curr_row + 1
    if next_row >= n:
        return False
    for col in range(k, k + m):
        if arr[next_row][col] != 0:
            return False
    return True

def go_row(curr_row):
    next_row = curr_row + 1
    for col in range(k, k + m):
        arr[curr_row][col] = 0
        arr[next_row][col] = 1

k -= 1
curr_row = 0
for col in range(k, k + m):
    arr[curr_row][col] = 1

while True:
    if check_next_row(curr_row):
        go_row(curr_row)
        curr_row += 1
    else:
        break

for line in arr:
    print(' '.join(map(str, line)))