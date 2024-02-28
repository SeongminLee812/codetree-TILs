from collections import deque

N, K, P, T = map(int, input().split())

MAX_TIME = 250
MAX_N = 100

arr = [
    [0] * (MAX_TIME + 1)
    for _ in range(MAX_N + 1)
]


for _ in range(T):
    t, x, y = map(int, input().split())
    arr[x][t] = y

# 감염 유부
is_sick = [0] * (MAX_N + 1)

q = deque()
# 최초 감염자
q.append((0, P))
is_sick[P] = 1

while q:
    # 감염시간, 감염된 사람 pop
    t, dev = q.popleft()

    # k initialize
    k = K

    for i in range(t, MAX_TIME + 1):
        if k and arr[dev][i] != 0:
            k -= 1
            is_sick[arr[dev][i]] = 1
            q.append((i, arr[dev][i]))

print(''.join(map(str, is_sick[1:N + 1])))