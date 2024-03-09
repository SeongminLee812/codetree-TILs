n, m = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

num_list = []

for row in range(n):
    _nums = []
    for col in range(n):
        _nums.append(arr[row][col])
    num_list.append(_nums)

for col in range(n):
    _nums = []
    for row in range(n):
        _nums.append(arr[row][col])
    num_list.append(_nums)

def is_happy(_nums):
    cnt, max_cnt = 1, 1
    for i in range(1, n):
        if _nums[i - 1] == _nums[i]:
            cnt += 1
        else:
            cnt = 1
        max_cnt = max(max_cnt, cnt)
    if max_cnt >= m:
        return True
    else:
        return False

ans = 0

for _nums in num_list:
    if is_happy(_nums):
        ans += 1

print(ans)