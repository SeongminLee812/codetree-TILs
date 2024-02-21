n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    if i % 2 == 0:
        now = arr[:i + 1]
        now.sort()
        print(now[i // 2], end=' ')