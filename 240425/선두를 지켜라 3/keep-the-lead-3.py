ㅠn, m = map(int, input().split())

A = [0] * 1002
B = [0] * 1002

pos = 1
for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        A[pos] = A[pos - 1] + v
        pos += 1

pos = 1
for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        B[pos] = B[pos - 1] +  v
        pos += 1

prev_status = -1
status = -1

ans = 0
for i in range(1, pos):
    if A[i] > B[i]:
        status = 1
    elif A[i] == B[i]:
        status = 2
    else: status = 0

    if prev_status != status:
        ans += 1
    prev_status = status

print(ans)