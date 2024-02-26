MAX_INT = 100000

color = [0] * (MAX_INT * 2 + 1)
w_count = [0] * (MAX_INT * 2 + 1)
b_count = [0] * (MAX_INT * 2 + 1)

n = int(input())

cur_point = 100000

for _ in range(n):
    move_count, direction = input().split()
    move_count = int(move_count)

    # r방향
    if direction == 'R':
        while move_count > 0:
            b_count[cur_point] += 1
            color[cur_point] = 'B'
            move_count -= 1

            if move_count:
                cur_point += 1

    if direction == 'L':
        while move_count > 0:
            w_count[cur_point] += 1
            color[cur_point] = 'W'
            move_count -= 1

            if move_count:
                cur_point -= 1

    # print('\t'.join(map(str, color[MAX_INT - 5: MAX_INT + 6])), '\t', 'cur_point', cur_point)
# 
# print('\t'.join(map(str, w_count[MAX_INT - 5: MAX_INT + 6])))
# print('\t'.join(map(str, b_count[MAX_INT - 5: MAX_INT + 6])))


white = 0
grey = 0
black = 0

for i in range(len(color)):
    if w_count[i] >= 2 and b_count[i] >= 2:
        grey += 1
    elif color[i] == 'W':
        white += 1
    elif color[i] == 'B':
        black += 1


print(white, black, grey)