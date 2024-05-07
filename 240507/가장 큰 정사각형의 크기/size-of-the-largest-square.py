n, m = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

ans = 0

for x in range(n):
    for y in range(m):
        # 좌측 상단 시작점을 x, y로 둠
        size = min(n - x, m - y)
        now_size = 0

        while size > 0:
            possible = True
            for j in range(size - 1, -1, -1):
                if arr[x + j][y + size - 1] == 0 or arr[x + size - 1][y + j] == 0:
                    size -= 1
                    possible = False
                    break
            if possible:
                now_size = size * size
                break

        ans = max(ans, now_size)

print(ans)