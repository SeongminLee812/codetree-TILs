# 현재 내 위치에서 count를 세서 인접한 1이 3개 이상이면 total + 1하기
# 전체 i, j에 대해서 수행
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y): # 범위 안에 들어오는 지 체크하는 함수
    return x >= 0 and x < n and y >= 0 and y < n

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

total = 0

for i in range(n):
    for j in range(n):
        x, y = i, j
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_range(nx, ny) and a[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            total += 1

print(total)