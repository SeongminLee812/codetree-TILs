n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

visited = [False] * n
visited[0] = True

def dfs(v):
    global ans
    for curr_v in graph[v]:
        if not visited[curr_v]:
            ans += 1
            visited[curr_v] = True
            dfs(curr_v)

ans = 0

dfs(0)
print(ans)