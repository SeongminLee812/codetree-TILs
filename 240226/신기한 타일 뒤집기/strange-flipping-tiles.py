MAX_INT = 100000
cur_point = 100000

color = [0] * (MAX_INT * 2 + 1)

# 시뮬레이션으로 풀기
n = int(input())

for _ in range(n):
    move_count, direction = input().split()
    move_count = int(move_count)

    if direction == 'L':
        while move_count > 0:
            color[cur_point] = 'W'
            move_count -= 1
            if move_count:
                cur_point -= 1

    if direction == 'R':
        while move_count > 0:
            color[cur_point] = 'B'
            move_count -= 1
            if move_count:
                cur_point += 1

white, black = 0, 0
for i in range(len(color)):
    if color[i] == 'W':
        white += 1
    elif color[i] == 'B':
        black += 1
print(white, black)