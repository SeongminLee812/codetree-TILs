from typing import *


def check(nums: List[int]) -> bool:
    f, s, t = nums
    # 1의 자리 숫자 확인
    while f != 0 or s != 0 or t != 0:
        if f % 10 + s % 10 + t % 10 >= 10:
            return False
        f //= 10
        s //= 10
        t //= 10
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
                ans = max(ans, arr[i] + arr[j] + arr[k])

print(ans)