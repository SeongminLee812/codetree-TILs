# 1. 몇일 지났는 지 확인
m1, d1, m2, d2 = map(int, input().split())
target = input()

month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
diff = 0
if m1 == m2:
    diff = d2 - d1
else:
    diff += month[m1] - d1
    diff += d2
    for i in range(m1 + 1, m2):
        diff += month[i]

day_dict = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6}

ans = 0
div, mod = divmod(diff, 7)

ans += div
target = day_dict[target]
if mod >= target:
    ans += 1
print(ans)