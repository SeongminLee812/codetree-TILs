n, m = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]


def get_square(num_k):
    # now_k를 1씩 늘려가며 k까지 대각선 구해나감
    dx_dy = []
    for now_k in range(1, num_k + 1):
        for direction in range(4):
            if direction == 0:
                for j in range(0, now_k + 1):
                    dx = -j
                    dy = -now_k + j
                    if (dx, dy) not in dx_dy:
                        dx_dy.append((dx, dy))

            elif direction == 1:
                for j in range(0, now_k + 1):
                    dx = -j
                    dy = now_k - j
                    if (dx, dy) not in dx_dy:
                        dx_dy.append((dx, dy))

            elif direction == 2:
                for j in range(0, now_k + 1):
                    dx = j
                    dy = -now_k + j
                    if (dx, dy) not in dx_dy:
                        dx_dy.append((dx, dy))

            else:
                for j in range(0, now_k + 1):
                    dx = j
                    dy = now_k - j
                    if (dx, dy) not in dx_dy:
                        dx_dy.append((dx, dy))
    return dx_dy

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

ans = 0

for k in range(n):
    # k == 0인 경우 예외처리
    cost = k * k + (k + 1) * (k + 1) if k > 0 else 1

    # 모든 x, y에 대하여 완전 탐색
    for x in range(n):
        for y in range(n):
            num_of_gold = 0

            start_x, start_y = x, y
            if arr[start_x][start_y]:
                num_of_gold += 1

            dx_dy = get_square(k)
            for dx, dy in dx_dy:
                nx, ny = start_x + dx, start_y + dy
                if in_range(nx, ny) and arr[nx][ny]:
                    num_of_gold += 1

            profit = num_of_gold * m
            if profit > cost:
                ans = max(ans, num_of_gold)

print(ans)