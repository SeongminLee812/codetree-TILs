import sys

n, m = map(int, input().split())

arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

def u_distance(first, second):
    x1, y1 = candidate[first]
    x2, y2 = candidate[second]
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

def calc():
    value = 0
    for i in range(m):
        for j in range(i + 1, m):
            distance = u_distance(i, j)
            value = max(value, distance)
    return value


def choose(num_index, cnt):
    global ans
    if cnt == m:
        ans = min(ans, calc())
        return
    if num_index == n:
        return

    # 선택
    candidate.append(arr[num_index])
    choose(num_index + 1, cnt + 1)
    candidate.pop()

    # 미선택
    choose(num_index + 1, cnt)

ans = sys.maxsize
candidate = []

choose(0, 0)

print(ans)