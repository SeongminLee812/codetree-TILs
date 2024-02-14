import sys

n = int(input())
sum_arr = list(map(int, input().split()))


def check(index):
    global visited, result
    if index == n:
        print(' '.join(map(str, result)))
        sys.exit()
        return True

    result[index] = sum_arr[index - 1] - result[index - 1]
    # print(f'\tindex: {index}')
    # print(f'result[index] :{result[index]} = {sum_arr[index - 1]} - {result[index - 1]}')
    if visited[result[index]]: # 지금 선택한 숫자가 이전에 사용된 숫자인 경우
        return False
    else:
        visited[result[index]] = True
        check(index + 1)

for i in range(1, n + 1):
    visited = [False] * (n + 1) # 숫자 1부터 1000까지 한번이라도 사용된 적이 있는 지 확인하는 배열
    result = [0] * n # 답이 되는 배열, 숫자를 순서대로 넣어줌
    result[0] = i
    visited[i] = True
    # print(f'try: {i}')
    check(1)