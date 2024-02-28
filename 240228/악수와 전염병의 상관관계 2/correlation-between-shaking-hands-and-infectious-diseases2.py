from collections import deque

N, K, P, T = map(int, input().split())

MAX_TIME = 250
MAX_N = 100

arr = [
    [0] * (MAX_TIME + 1)
    for _ in range(MAX_N + 1)
]

already_meet = [
    [0] * (MAX_N + 1)
    for _ in range(MAX_N + 1)
]

for _ in range(T):
    t, x, y = map(int, input().split())
    arr[x][t] = y
    arr[y][t] = x

for row in arr[1:6]:
    print(row[1:8])

# 감염 유무
is_sick = [0] * (MAX_N + 1)

q = deque()
# 최초 감염자
q.append((0, P))
is_sick[P] = 1

while q:
    # 감염시간, 감염된 사람 pop
    infected_time, dev = q.popleft()

    # k initialize
    k = K

    for t in range(infected_time, MAX_TIME + 1):
        if k and arr[dev][t] != 0 and not already_meet[dev][arr[dev][t]]:
            k -= 1
            is_sick[arr[dev][t]] = 1
            already_meet[dev][arr[dev][t]] = 1
            q.append((t, arr[dev][t]))

print(''.join(map(str, is_sick[1:N + 1])))