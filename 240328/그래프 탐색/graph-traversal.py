n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [False] * (n + 1)
# 1번은 정점 수에서 제외해야하므로 방문처리
visited[1] = True
cnt = 0

def dfs(curr_ver):
    #
    global cnt
    for vertax in graph[curr_ver]:
        if not visited[vertax]:
            visited[vertax] = True
            cnt += 1
            dfs(vertax)

dfs(1)
print(cnt)