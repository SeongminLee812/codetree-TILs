import sys

n, b = map(int, input().split())

p = [0] * n
s = [0] * n
total = [0] * n
for i in range(n):
    p[i], s[i] = map(int, input().split())
    total[i] = p[i] + s[i]

ans = -sys.maxsize

for i in range(n):
    total[i] = p[i] // 2 + s[i]
    temp = total[:]

    temp.sort()
    cnt = 0
    student = 0
    now = 0
    while True:
        now += temp[student]
        if now > b or student == n:
            break
        cnt += 1
        student += 1
    ans = max(ans, student)
    
    total[i] *= 2


print(ans)