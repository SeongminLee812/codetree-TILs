import sys

n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = []
def search_min_value(array):
    min_value = 10001
    for i, j in enumerate(array):
        min_value = min(min_value, arr[i][j])
    return min_value

def choose(select_idx):
    global ans
    if select_idx == n + 1:
        min_value = search_min_value(selected)
        ans = max(ans, min_value)
        return

    for i in range(n):
        if i in visited:
            continue
        selected.append(i)
        visited.append(i)
        choose(select_idx + 1)
        selected.pop()
        visited.pop()


selected = []
ans = 0

choose(1)
print(ans)