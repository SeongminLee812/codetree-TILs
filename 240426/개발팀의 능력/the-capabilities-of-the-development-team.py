import sys

arr = list(map(int, input().split()))

ans = sys.maxsize
total = sum(arr)

for i in range(5 - 1):
    for j in range(i + 1, 5):
        for k in range(5):
            if k == i or k == j:
                continue
            team_a = arr[i] + arr[j]
            team_b = arr[k]
            team_c = total - team_a - team_b
            if team_a == team_b or team_a == team_c or team_b == team_c:
                continue
            diff = max([team_a, team_b, team_c]) - min([team_a, team_b, team_c])
            ans = min(diff, ans)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)