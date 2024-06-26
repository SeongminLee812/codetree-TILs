n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
print(arr)

dx = [1, 1, -1, -1]
dy = [-1, 1, 1, -1]

ans = 0
m = n - 1

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

for i in range(n):
    for j in range(n):
        start_x, start_y = i, j
        start_point = arr[i][j]

        for first_step in range(1, n):
            first_x = start_x + dx[0] * first_step
            first_y = start_y + dy[0] * first_step
            if not in_range(first_x, first_y):
                continue
            first_point = start_point + arr[first_x][first_y]

            for second_step in range(1, n):
                second_x = first_x + dx[1] * second_step
                second_y = first_y + dy[1] * second_step
                if not in_range(second_x, second_y):
                    continue
                second_point = first_point + arr[second_x][second_y]

                for third_step in range(1, n):
                    third_x = second_x + dx[2] * third_step
                    third_y = second_y + dy[2] * third_step
                    if not in_range(third_x, third_y):
                        continue

                    third_point = second_point + arr[third_x][third_y]

                    for forth_step in range(1, n):
                        forth_x = third_x + dx[3] * forth_step
                        forth_y = third_y + dy[3] * forth_step
                        if not in_range(forth_x, forth_y):
                            continue
                        if forth_x == start_x and forth_y == start_y:
                            print(f'path = {start_x, start_y}, {first_x, first_y}, {second_x, second_y}, {third_x, third_y}, {forth_x, forth_y}')
                            ans = max(ans, third_point)

print(ans)