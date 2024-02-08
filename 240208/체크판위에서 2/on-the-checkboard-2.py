r, c = map(int, input().split())
chess = [input().split() for _ in range(r)]

ans = 0


first = chess[0][0]
for k in range(1, r - 2):
    for l in range(1, c - 2):
        if first != chess[k][l]:
            second = chess[k][l]
            for z in range(k + 1, r - 1):
                for x in range(l + 1, c - 1):
                    if second != chess[z][x]:
                        third = chess[z][x]
                        if chess[r - 1][c - 1] != third:
                            ans += 1
                    

print(ans)