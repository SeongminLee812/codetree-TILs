import copy
from collections import deque

n, k, m = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]


start_point = []

for _ in range(k):
    r, c = map(int, input().split())
    start_point.append((r - 1, c - 1))

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or now_arr[x][y] != 0:
        return False
    return True

def bfs():
    global blocks
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        blocks += 1

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))

# 일일히 모든 돌의 조합을 계산해서 치운 후 확인해야함.
def choose(stone_index, cnt):
    if cnt == m:
        candidate.append(combination.copy())
        # 그냥 candidate.append(combination) 할 시, combination의 참조만 추가하게됨
        # 즉, 마지막에 combination이 []가 되므로 []만 추가되어 있었던 것임!
        return
    if stone_index == stone_cnt:
        return

    # 선택
    combination.append(stones[stone_index])
    choose(stone_index + 1, cnt + 1)
    combination.pop()

    choose(stone_index + 1, cnt)


# 모든 돌의 위치 담기
stones = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            stones.append((i, j))

candidate = []
combination = []
stone_cnt = len(stones)
choose(0, 0)

blocks = 0
ans = 0

if candidate:
    for remove_stones in candidate:
        # 초기화
        blocks = 0
        now_arr = copy.deepcopy(arr)
        q = deque(start_point)
        visited = [
            [False] * n
            for _ in range(n)
        ]
        for i, j in q:
            visited[i][j] = True

        for i, j in remove_stones:
            now_arr[i][j] = 0

        bfs()
        ans = max(blocks, ans)
else:
    now_arr = copy.deepcopy(arr)
    q = deque(start_point)
    bfs()
    ans = blocks

print(ans)