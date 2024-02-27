MAX_INT = 1000000

a_move = [0] * (MAX_INT + 1)
b_move = [0] * (MAX_INT + 1)

n, m = map(int, input().split())

times = 0
pos = 0
finished_time = 0

for _ in range(n):
    direction, move = input().split()
    move = int(move)
    finished_time += move
    if direction == 'R':
        for i in range(move):
            times += 1
            pos += 1
            a_move[times] = pos

    else:
        for i in range(move):
            times += 1
            pos -= 1
            a_move[times] = pos

# initialize
times = 0
pos = 0

for _ in range(m):
    direction, move = input().split()
    move = int(move)
    if direction == 'R':
        for i in range(move):
            times += 1
            pos += 1
            b_move[times] = pos

    else:
        for i in range(move):
            times += 1
            pos -= 1
            b_move[times] = pos

ans = -1
for i in range(1, finished_time + 1):
    if a_move[i] == b_move[i]:
        ans = i
        break
print(ans)