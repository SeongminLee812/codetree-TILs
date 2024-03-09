# 가장 마지막 숫자는 우선 정렬되었다고 가정함.
# 가장 앞 숫자는 항상 이미 정렬된 자리들 사이로 들어가야 함.
# 검사는 i가 i번째 위치에 있는 지만 검사하면 되기 때문에 O(N)에 검사 가능

n = int(input())
arr = list(map(int, input().split()))

sorted_start = n - 1

for i in range(n - 1, 0, -1):
    if arr[i - 1] < arr[i]:
        sorted_start = i - 1
    else:
        break

def is_sorted():
    for i in range(n):
        if arr[i] != i + 1:
            return False
    return True

cnt = 0

while not is_sorted():
    # print(arr)
    if cnt > 10:
        break
    key = arr[0]
    for i in range(1, sorted_start):
        arr[i - 1] = arr[i]

    j = sorted_start
    while j < n and arr[j] < key:
        arr[j - 1] = arr[j]
        j += 1
    arr[j - 1] = key

    sorted_start -= 1
    cnt += 1

print(cnt)