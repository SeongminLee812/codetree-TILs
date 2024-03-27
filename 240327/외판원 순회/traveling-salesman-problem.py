import sys

n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [False] * n
path = [0]

def calc_cost(path):
    local_path = path[:] + [0]
    total = 0
    prev_i = 0
    for i in range(1, n + 1):
        if arr[local_path[prev_i]][local_path[i]] == 0:
            return sys.maxsize
        value = arr[local_path[prev_i]][local_path[i]]
        total += value
        prev_i = i
    return total

def choose(curr_index):
    global ans
    if curr_index == n - 1:
        ans = min(ans, calc_cost(path))
        return

    for i in range(1, n):
        if visited[i]:
            continue
        visited[i] = True
        path.append(i)

        choose(curr_index + 1)
        visited[i] = False
        path.pop()

ans = sys.maxsize
choose(0)
print(ans)