n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

# 직사각형은 윗변길이 == 아랫변길이, 왼쪽변길이 == 오른쪽변길이
def get_score(x, y, k, l):
    dxs = [1, 1, -1, -1]
    dys = [-1, 1, 1, -1]
    move_nums = [k, l, k, l]
    score = 0

    for dx, dy, move_num in zip(dxs, dys, move_nums):
        for _ in range(move_num):
            x = x + dx
            y = y + dy

            if not in_range(x, y):
                return 0

            score += arr[x][y]

    return score

ans = 0

# 모든 시작점에 대해
# 모든 가능한 변의 길이 탐색

for i in range(n):
    for j in range(n):
        for k in range(1, n):
            for l in range(1, n):
                ans = max(ans, get_score(i, j, k, l))

print(ans)