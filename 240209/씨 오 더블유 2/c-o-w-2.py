n = int(input())
a = input()

ans = 0
for i in range(n):
    if a[i] == 'C':
        for j in range(i + 1, n):
            if a[j] == 'O':
                for k in range(j + 1, n):
                    if a[k] == 'W':
                        ans += 1

print(ans)