from collections import deque

q1 = deque()
q2 = deque()

n, k = map(int, input().split())

for i in range(1, n +1):
    q1.append(i)

while q1:
    for _ in range(k - 1):
        q1.append(q1.popleft())
    print(q1.popleft(), end=' ')