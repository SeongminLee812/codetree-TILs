import sys

arr = list(map(int, input().split()))
all_sum = sum(arr)
ans = sys.maxsize

for i in range(6):
    for j in range(6):
        if i == j:
            continue

        for k in range(6):
            if i == k or j == k:
                continue

            for l in range(6):
                if i == l or j == l or k == l:
                    continue
                team1 = arr[i] + arr[j]
                team2 = arr[k] + arr[l]
                team3 = all_sum - team1 - team2
                diff = max([team1, team2, team3]) - min([team1, team2, team3])
                ans = min(ans, diff)

print(ans)