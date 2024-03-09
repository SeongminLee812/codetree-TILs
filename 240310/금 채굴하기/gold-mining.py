n, m = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]


def get_square(num_k, x, y):
    # now_k를 1씩 늘려가며 k까지 대각선 구해나감
    dx_dy = []
    for i in range(n):
        for j in range(n):
            if abs(x - i) + abs(y - j) <= num_k:
                dx_dy.append((i, j))
    return dx_dy

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

ans = 0

for k in range(n + 1):
    # k == 0인 경우 예외처리
    cost = k * k + (k + 1) * (k + 1) if k > 0 else 1

    # 모든 x, y에 대하여 완전 탐색
    for x in range(n):
        for y in range(n):
            num_of_gold = 0

            start_x, start_y = x, y

            dx_dy = get_square(k, start_x, start_y)
            for nx, ny in dx_dy:
                if in_range(nx, ny) and arr[nx][ny]:
                    num_of_gold += 1

            profit = num_of_gold * m
            if profit >= cost:
                ans = max(ans, num_of_gold)

print(ans)