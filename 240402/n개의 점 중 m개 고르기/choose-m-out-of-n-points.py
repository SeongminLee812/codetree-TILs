import sys

n, m = map(int, input().split())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

def get_dist(v1, v2):
    return (v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2

def calc(chosen_indices):
    value = 0
    for i in range(m):
        for j in range(i + 1, m):
            value = max(get_dist(arr[chosen_indices[i]], arr[chosen_indices[j]]), value)
    return value

def choose(num_index, cnt):
    global ans

    if cnt == m:
        ans = min(ans, calc(indice))
        return

    if num_index == n:
        return

    indice.append(num_index)
    choose(num_index + 1, cnt + 1)
    indice.pop()

    choose(num_index + 1, cnt)


ans = sys.maxsize
indice = []
choose(0, 0)
print(ans)