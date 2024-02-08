import sys

n = int(input())
checkpoints = []
for _ in range(n):
    x, y = map(int, input().split())
    checkpoints.append((x, y))

ans = sys.maxsize

for i in range(1, n - 1):
    without_check = checkpoints[:i] + checkpoints[i + 1:]
    distance = 0
    for i in range(len(without_check) - 1):
        distance += abs(without_check[i][0] - without_check[i + 1][0])
        distance += abs(without_check[i][1] - without_check[i + 1][1])
    ans = min(ans, distance)

print(ans)