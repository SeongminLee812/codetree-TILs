from collections import deque

n, k, u, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# k개의 위치값이 담긴 배열
ans = []

c = [[False] * n for _ in range(n)]

def initialze():
    visited = [[False] * n for _ in range(n)]
    return visited, 0

def choose(num):
    global ans, result
    if num == k:
        start_city_q = deque()
        visited, goable_cities = initialze()

        for elem in ans:
            start_city_q.append(elem)
            visited[elem[0]][elem[1]] = True
        goable_cities = bfs(start_city_q, visited, goable_cities)
        result = max(result, goable_cities)
        return

    for i in range(n):
        for j in range(n):
            if not c[i][j]:
                c[i][j] = True
                ans.append((i, j))
                choose(num + 1)
                ans.pop()
                c[i][j] = False

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y, nx, ny, visited):
    if not in_range(nx, ny):
        return False
    if visited[nx][ny]:
        return False
    if abs(a[nx][ny] - a[x][y]) < u or abs(a[nx][ny] - a[x][y]) > d:
        return False
    return True


def bfs(q, visited, goable_cities):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        goable_cities += 1
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if can_go(x, y, nx, ny, visited):
                visited[nx][ny] = True
                q.append((nx, ny))
    return goable_cities

result = 0
choose(0)
print(result)