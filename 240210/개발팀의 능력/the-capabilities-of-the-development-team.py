import sys

arr = list(map(int, input().split()))

all_sum = sum(arr)
INT_MAX = sys.maxsize
ans = INT_MAX

for i in range(5):
    for j in range(5):
        if i == j:
            continue

        for k in range(5):
            if i == k or j == k:
                continue
            team1 = arr[i] + arr[j]
            team2 = arr[k]
            team3 = all_sum - team1 - team2
            if team1 == team2 or team1 == team3 or team2 == team3:
                continue
            diff = max([team1, team2, team3]) - min([team1, team2, team3])
            ans = min(ans, diff)

if ans == INT_MAX:
    print(-1)
else:
    print(ans)