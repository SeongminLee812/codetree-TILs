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
    cnt = 1
    if len(_nums) == 1:
        if cnt >= m:
            return True
    for i in range(1, n):
        if _nums[i - 1] == _nums[i]:
            cnt += 1
        if _nums[i - 1] != _nums[i] or i == n - 1:
            if cnt >= m:
                return True
            cnt = 1

    return False

ans = 0

for _nums in num_list:
    if is_happy(_nums):
        ans += 1

print(ans)