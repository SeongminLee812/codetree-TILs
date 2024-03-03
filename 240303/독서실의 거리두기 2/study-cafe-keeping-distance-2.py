n = int(input())
arr = list(map(int, list(input())))

# 오른쪽과 왼쪽 둘 다 비어있는 경우
if arr[0] == 0 and arr[-1] == 0:
    # 오른쪽과의 거리, 왼쪽과의 거리, 중간에 있는 최대거리 셋 다 구해야함
    left_distance = 0
    prev_idx = 0
    longest_distance = 0
    right_distance = 0
    for i in range(n):
        # 처음 1 만난 경우
        if arr[i] == 1 and prev_idx == 0:
            left_distance = i
            prev_idx = i
        elif arr[i] == 1 and prev_idx != 0:
            dist = i - prev_idx
            longest_distance = (max(longest_distance, dist))
            prev_idx = i
        elif i == n - 1:
            right_distance = i - prev_idx
    ans = max(left_distance, right_distance, longest_distance // 2)
# 왼쪽만 비어있는 경우
elif arr[0] == 0 and arr[-1] == 1:
    # 왼쪽과의 거리, 중간에 있는 최대거리
    left_distance = 0
    prev_idx = 0
    longest_distance = 0
    for i in range(n):
        # 처음 1 만난 경우
        if arr[i] == 1 and prev_idx == 0:
            left_distance = i
            prev_idx = i
        elif arr[i] == 1 and prev_idx != 0:
            dist = i - prev_idx
            longest_distance = (max(longest_distance, dist))
            prev_idx = i
    ans = max(left_distance, longest_distance // 2)

elif arr[0] == 1 and arr[-1] == 0:
    # 오른쪽과의 거리, 중간에 있는 최대거리
    longest_distance = 0
    right_distance = 0
    prev_idx = 0
    for i in range(n):
        if arr[i] == 1:
            dist = i - prev_idx
            longest_distance = max(longest_distance, dist)
            prev_idx = i
        if i == n - 1:
            right_distance = i - prev_idx
    ans = max(longest_distance // 2, right_distance)
# 둘 다 차있는 경우
else:
    # 최대거리
    longest_distance = 0
    prev_idx = 0
    for i in range(n):
        if arr[i] == 1:
            dist = i - prev_idx
            longest_distance = max(longest_distance, dist)
            prev_idx = i
    ans = longest_distance // 2

# 새로운 인원 투입 전에 가장 짧은 거리가 있는 경우
shortest_dist = 1001
prev_idx = 0
for i in range(1, n):
    if arr[i] == 1:
        dist = i - prev_idx
        shortest_dist = min(shortest_dist, dist)
        prev_idx = i

ans = min(ans, shortest_dist)
print(ans)