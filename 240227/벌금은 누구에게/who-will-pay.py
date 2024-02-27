n, m, k = map(int, input().split())

left = [0] + [k] * n

def check():
    for i in range(1, n):
        if left[i] == 0:
            return True
    return False

ans = -1
for _ in range(m):
    number = int(input())
    left[number] -= 1
    if left[number] == 0:
        ans = number
        break

print(ans)