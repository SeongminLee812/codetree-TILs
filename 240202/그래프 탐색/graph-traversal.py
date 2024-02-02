n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
visited[1] = True

def dfs(v):
    global ans
    for curr_v in graph[v]:
        if not visited[curr_v]:
            ans += 1
            visited[curr_v] = True
            dfs(curr_v)

ans = 0

dfs(1)
print(ans)