from collections import defaultdict

x, y = map(int, input().split())

def check(num):
    num = str(num)
    count_dict = defaultdict(int)
    for i in range(len(num)):
        count_dict[num[i]] += 1

    values = list(count_dict.values())
    if len(values) != 2:
        return False
    if values[0] != 1 and values[1] != 1:
        return False
    return True

ans = 0
for i in range(x, y + 1):
    if check(i):
        ans += 1

print(ans)