n = int(input())
arr = [
    int(input())
    for _ in range(n)
]

s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# 뺄 블럭 표시
for i in range(s1 - 1, e1):
    arr[i] = 0

# 블럭 제외
temp = [0] * n
temp_index = 0
for i in range(n):
    if arr[i]:
        temp[temp_index] = arr[i]
        temp_index += 1

for i in range(n):
    arr[i] = temp[i]

# 두번째 뺄 블럭 표시
for i in range(s2 - 1, e2):
    arr[i] = 0

temp = [0] * n
temp_index = 0
for i in range(n):
    if arr[i]:
        temp[temp_index] = arr[i]
        temp_index += 1

for i in range(n):
    arr[i] = temp[i]

print(temp_index)
for i in range(temp_index):
    print(arr[i])