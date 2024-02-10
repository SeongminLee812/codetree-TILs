n = int(input())
dial1 = list(map(int, input().split()))
dial2 = list(map(int, input().split()))

def check(nums, dial):
    ok = True
    for i in range(3):
        if abs(nums[i] - dial[i]) > 2 and abs(nums[i] - dial[i]) < n - 2:
            ok = False
    return ok

total = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if check([i, j, k], dial1) or check([i, j, k], dial2):
                total += 1

print(total)