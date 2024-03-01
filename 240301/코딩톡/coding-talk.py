n, m, p = map(int, input().split())

arr = [1] * n

for i in range(m):
    person, nums = input().split()
    if i >= p - 1:
        person = ord(person) - ord('A')
        arr[person] = 0

for i in range(n):
    if arr[i]:
        char = chr(ord('A') + i)
        print(char, end=' ')