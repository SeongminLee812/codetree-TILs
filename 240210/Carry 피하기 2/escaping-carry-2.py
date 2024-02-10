from typing import *

def to_list(num: int) -> List[str]:
    return list(str(num))

def check(nums: List[int]) -> bool:
    length = len(str(max(nums)))
    f, s, t = map(to_list, nums)
    nums = [f, s, t]

    for i in range(3):
        while len(nums[i]) < length:
            nums[i] = ['0'] + nums[i]

    for i in range(length):
        if int(nums[0][i]) + int(nums[1][i]) + int(nums[2][i]) >= 10:
            return False
    return True

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

ans = -1

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if check([arr[i], arr[j], arr[k]]):
                ans = arr[i] + arr[j] + arr[k]

print(ans)