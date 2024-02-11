n, c, g, h = map(int, input().split())

work_load = []

max_tb = 0

for _ in range(n):
    ta, tb = map(int, input().split())
    work_load.append((ta, tb))
    max_tb = max(max_tb, tb)

def get_score(ta, tb, temperature):
    if temperature < ta:
        return c
    if temperature > tb:
        return h
    else:
        return g

ans = 0
for i in range(0, max_tb + 2):
    finished = 0
    for ta, tb in work_load:
        finished += get_score(ta, tb, i)
    ans = max(finished, ans)

print(ans)