# 1 k 후보 뽑기
# 2 k 후보들을 for loop돌면서 시작 q로 사용
from collections import deque

n, k, u, d = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

# k 뽑기 (조합)
def choose(num_index, cnt):
    if cnt == k:
        candidate.append(combi.copy())
        return
    if num_index == city_cnt:
        return

    combi.append(city_positions[num_index])
    choose(num_index + 1, cnt + 1)
    combi.pop()

    choose(num_index + 1, cnt)

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y, value):
    if not in_range(x, y):
        return False
    if visited[x][y]:
        return False
    if d < abs(arr[x][y] - value) or u > abs(arr[x][y] - value):
        return False
    return True


def bfs():
    global cities
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, arr[x][y]):
                visited[nx][ny] = True
                cities += 1
                q.append((nx, ny))


if __name__ == '__main__':
    candidate = []
    combi = []
    city_positions = []
    for i in range(n):
        for j in range(n):
            city_positions.append((i, j))
    city_cnt = len(city_positions)
    choose(0, 0)

    # candidate 순회
    max_city = 0

    for start_pos in candidate:
        q = deque(start_pos)
        visited = [
            [False] * n
            for _ in range(n)
        ]
        cities = 0
        for i, j in start_pos:
            visited[i][j] = True
            cities += 1
        bfs()
        max_city = max(cities, max_city)

    print(max_city)