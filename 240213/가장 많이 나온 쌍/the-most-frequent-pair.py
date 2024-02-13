n, m = map(int, input().split())

arr = []
for _ in range(m):
    a, b = map(int, input().split())
    arr.append((a, b))



ans = 0

for i in range(m - 1):
    cnt = 1
    for j in range(i + 1, m):
        i_a, i_b = arr[i]
        j_a, j_b = arr[j]
        if (i_a == j_a or i_a == j_b) and (i_b == j_a or i_b == j_b):
            cnt += 1
    ans = max(ans, cnt)

print(ans)