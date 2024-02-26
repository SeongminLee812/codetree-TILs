MAX_INT = 100000

color = [0] * (MAX_INT * 2 + 1)
w_count = [0] * (MAX_INT * 2 + 1)
b_count = [0] * (MAX_INT * 2 + 1)

n = int(input())

cur_point = 100000

# print('\t'.join(map(str, (i for i in range(-5, 6)))))
# print('=\t'*11)
for _ in range(n):
    move_count, direction = input().split()
    move_count = int(move_count)
    move_count -= 1

    # r방향
    if direction == 'R':
        b_count[cur_point] += 1
        color[cur_point] = 'B'
        for i in range(cur_point + 1, cur_point + move_count + 1):
            b_count[i] += 1
            color[i] = 'B'
        cur_point += move_count

    if direction == 'L':
        w_count[cur_point] += 1
        color[cur_point] = 'W'
        for i in range(cur_point - 1, cur_point - move_count - 1, -1):
            w_count[i] += 1
            color[i] = 'W'
        cur_point -= move_count
#     print('\t'.join(map(str, color[MAX_INT - 5: MAX_INT + 6])), '\t', 'cur_point', cur_point)
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