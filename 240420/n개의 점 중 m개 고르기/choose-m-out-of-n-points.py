import sys

n, m = map(int, input().split())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

def distance(point_1, point_2):
    return (point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2

def calc(point_list):
    max_distance = 0
    for i in range(m - 1):
        for j in range(i + 1, m):
            max_distance = max(max_distance, distance(point_list[i], point_list[j]))
    return max_distance

# n 개 중에 m개 고르기
def binary_select(num_index, selected, cnt):
    global ans
    if cnt == m:
        ans = min(ans, calc(selected))
        return

    if num_index == n:
        return

    binary_select(num_index + 1, selected + [arr[num_index]], cnt + 1)
    binary_select(num_index + 1, selected, cnt)

ans = sys.maxsize
binary_select(0, [], 0)
print(ans)