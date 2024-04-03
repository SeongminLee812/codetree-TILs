n, t = map(int, input().split())

line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))
line3 = list(map(int, input().split()))

for _ in range(t):
    temp = line3[-1]

    for i in range(n - 1, 0, -1):
        line3[i] = line3[i - 1]
    line3[0] = line2[-1]
    for i in range(n - 1, 0, -1):
        line2[i] = line2[i - 1]
    line2[0] = line1[-1]
    for i in range(n - 1, 0, -1):
        line1[i] = line1[i - 1]
    line1[0] = temp

print(' '.join(map(str, line1)))
print(' '.join(map(str, line2)))
print(' '.join(map(str, line3)))