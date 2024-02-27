MAX_INT = int(1e6)

a_move = [0] * (MAX_INT + 1)
b_move = [0] * (MAX_INT + 1)


n, m = map(int, input().split())

a_total_time = 0
current = 1

for _ in range(n):
    move, direction = input().split()
    move = int(move)
    a_total_time += move

    now_move = 1 if direction == 'R' else -1
    for _ in range(move):
        a_move[current] = a_move[current - 1] + now_move
        current += 1

current = 1
b_total_time = 0
for _ in range(m):
    move, direction = input().split()
    move = int(move)
    b_total_time += move

    now_move = 1 if direction == 'R' else -1
    for _ in range(move):
        b_move[current] = b_move[current - 1] + now_move
        current += 1

if a_total_time > b_total_time:
    total_time = a_total_time
    for i in range(b_total_time + 1, total_time + 1):
        b_move[i] = b_move[b_total_time]
elif b_total_time > a_total_time:
    total_time = b_total_time
    for i in range(a_total_time + 1, total_time + 1):
        a_move[i] = a_move[a_total_time]
else:
    total_time = a_total_time

ans = 0
for i in range(1, total_time + 1):
    if a_move[i - 1] != b_move[i - 1] and a_move[i] == b_move[i]:
        ans += 1

print(ans)