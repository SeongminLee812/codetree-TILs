n, m = map(int, input().split())

visited = [False] * (n + 1)

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def dfs(v):
    global ans
    for curr_v in graph[v]:
        if not visited[curr_v]:
            visited[curr_v] = True
            ans += 1
            dfs(curr_v)

ans = 0
dfs(1)
print(ans)