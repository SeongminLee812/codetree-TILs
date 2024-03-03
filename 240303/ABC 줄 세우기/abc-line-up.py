n = int(input())
arr = list(input().split())
# 계산의 편의를 위해 arr을 다 숫자로 바꿈

for i in range(n):
    arr[i] = ord(arr[i]) - ord('A')
print(arr)

def is_sorted():
    for i in range(n):
        if arr[i] != i:
            return False
    return True

ans = 0
while not is_sorted():
    for j in range(n - 1, 0, -1):
        if arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            ans += 1


print(ans)