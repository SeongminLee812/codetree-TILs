n = int(input())
directions_list = [list(map(int, input().split())) for _ in range(n)]

placed = [0, 0, 0]

def swap(a, b):
    placed[a], placed[b] = placed[b], placed[a]

ans = 0
for i in range(3):
    placed[i] = 1
    score = 0
    for a, b, c in directions_list:
        a -= 1
        b -= 1
        c -= 1
        swap(a, b)
        if placed[c] == 1:
            score += 1
    ans = max(ans, score)
    placed = [0, 0, 0]

print(ans)