from collections import deque

N, K, P, T = map(int, input().split())
MAX_TIME = 250
MAX_PEOPLE = 100

# record handshake, row: people, col: time, record: y
handshake = [
    [0] * (MAX_TIME + 1)
    for _ in range(MAX_PEOPLE + 1)
]

# record remain k
k_list = [K] * (MAX_PEOPLE + 1)

# infect information
result = [0] * (MAX_PEOPLE + 1)
max_dev = 0

for _ in range(T):
    t, x, y = map(int, input().split())
    handshake[x][t] = y
    handshake[y][t] = x

# already meet(3d array) / to drop duplicated
already = [[
    [0] * (MAX_PEOPLE + 1)
    for _ in range(MAX_PEOPLE + 1)
] for _ in range(MAX_TIME + 1)]

# queue which I will
q = deque()
q.append((0, P))
result[P] = 1

while q:
    start_time, x_dev = q.popleft()

    for time in range(start_time, MAX_TIME + 1):
        # 아직 x개발자의 k가 남았고, y 를 만났고, 처리가 안된 경우
        y_dev = handshake[x_dev][time]
        if (k_list[x_dev] > 0) and (y_dev != 0) and (already[time][x_dev][y_dev] == 0):
            # 처리 배열
            already[time][x_dev][y_dev] = 1
            already[time][y_dev][x_dev] = 1
            # 만난 시간을 넣어줘야함
            # 시간 순서로 들어가야한다.
            q.append((time, y_dev))
            # 이미 y도 감염된 경우에는 y의 k도 빼줌
            if result[y_dev]:
                k_list[y_dev] -= 1
            result[y_dev] = 1
            k_list[x_dev] -= 1
        if k_list[x_dev] == 0:
            break

print(''.join(map(str, result[1:N + 1])))