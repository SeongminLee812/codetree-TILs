n = int(input())
arr = list(input().split())
# 계산의 편의를 위해 arr을 다 숫자로 바꿈

for i in range(n):
    arr[i] = ord(arr[i]) - ord('A')

def is_sorted():
    for i in range(n):
        if arr[i] != i:
            return False
    return True

# 정렬 방법
# 가장 작은 원소 먼저 찾음
# 가장 작은 원소의 왼쪽과 차례로 비교해가며 swap

def selection_sort():
    cnt = 0
    min_idx = 0
    min_val = 27
    sorted_list = [False] * n

    while not is_sorted():
        # for i in range(n):
        #     if not sorted_list[i] and arr[i] < min_val:
        #         min_idx = i
        #         min_val = arr[i]

        for j in range(n - 1, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                cnt += 1

    return cnt

ans = selection_sort()
print(ans)