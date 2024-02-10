from typing import *


def check(nums: List[int]) -> bool:
    f, s, t = nums
    # 1의 자리 숫자 확인
    if f % 10 + s % 10 + t % 10 >= 10:
        return False
    # 10의 자리 숫자
    if f % 100 // 10 + s % 100 // 10 + t % 100 // 10:
        return False
    # 100의 자리 숫자
    if f % 1000 // 100 + s % 1000 // 100 + t % 1000 // 100:
        return False
    if f % 10000 // 1000 + s % 10000 // 1000 + t % 10000 // 1000:
        return False


n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

ans = -1

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if check([arr[i], arr[j], arr[k]]):
                ans = max(ans, arr[i] + arr[j] + arr[k])

print(ans)