# 각 숫자가 폭탄의 key값으로 주어지며,
# 그 숫자가 연속하여 m번 이상 등장 시 연속된 폭탄은 전부 터짐
# m개 이상 연속한 폭탄이 존재하지 않을 때까지 반복

# 풀이
## 모든 배열을 순회하면서 검사. 연속된 부분이 발견되면 start_idx, end_idx를 표시하며 이동
## 연속된 부분이 끝나고 다른 숫자가 나왔을 때, end_idx - start_idx >= m 인 경우 체크 후 제거
## m이상인 경우가 없는 경우 False반환 후 반복 종료

n, m = map(int, input().split())
arr = [
    int(input())
    for _ in range(n)
]

def search():
    start_idx = 0
    cnt = 1
    for i in range(n - 1):
        if arr[i] == arr[i + 1]:
            cnt += 1
        else:
            if cnt >= m:
                return start_idx, cnt
            start_idx = i + 1
            cnt = 1

    if cnt >= m:
        return start_idx, cnt

    return False

def bomb():
    global end_of_array
    bomb_range = search()
    if not bomb_range:
        return False
    start_idx, cnt = bomb_range

    temp_array = [0] * end_of_array

    end_of_temp_array = 0
    for i in range(end_of_array):
        if i < start_idx or i >= start_idx + cnt:
            temp_array[end_of_temp_array] = arr[i]
            end_of_temp_array += 1

    for i in range(end_of_temp_array + 1):
        arr[i] = temp_array[i]

    end_of_array = end_of_temp_array
    return True

end_of_array = n

while True:
    if not bomb():
        break

print(end_of_array)
for i in range(end_of_array):
    print(arr[i])