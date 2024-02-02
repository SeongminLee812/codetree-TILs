n, m = map(int, input().split())

visited = [False] * (n + 1)

graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for line in graph:
    print(line)

def dfs(v):
    global ans
    print(v, end = '')
    for curr_v in graph[v]:
        if graph[v][curr_v] == 1 and not visited[curr_v]:
            visited[curr_v] = True
            ans += 1
            dfs(curr_v)

ans = 0
dfs(1)
print(ans)