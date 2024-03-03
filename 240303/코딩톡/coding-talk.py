n, m, p = map(int, input().split())

arr = [1] * n

for i in range(1, m + 1):
    person, nums = input().split()
    nums = int(nums)
    if i >= p:
        person = ord(person) - ord('A')
        arr[person] = 0

    if i == p and nums == 0:
        for j in range(n):
            arr[j] = 0

for i in range(n):
    if arr[i]:
        char = chr(ord('A') + i)
        print(char, end=' ')