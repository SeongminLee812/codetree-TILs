class Number():
    def __init__(self, number, index):
        self.number = number
        self.index = index

n = int(input())
arr = list(map(int, input().split()))

nums = [
    Number(val, idx)
    for idx, val in enumerate(arr)
]
answer = [0] * n

nums.sort(key=lambda x: (x.number, x.index))

for i, obj in enumerate(nums):
    answer[obj.index] = i + 1

print(' '.join(map(str, answer)))