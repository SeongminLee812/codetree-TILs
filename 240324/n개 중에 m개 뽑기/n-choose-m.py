n, m = map(int, input().split())

arr = [False] * (n + 1)

def print_answer():
    for i in range(1, n + 1):
        if arr[i]:
            print(i, end=' ')
    print()

def choose(num_index, selected_cnt):
    """
    숫자 후보 중 num_index 번째의 숫자를 뽑을 지 말지 결정하는 함수
    m개 만큼 뽑으면 종료
    :param num_index: 주어진 숫자 후보 중 몇번 째 숫자를 고를 건지 말건지
    :param selected_cnt: 현재까지 선택된 수의 개수
    :return:
    """
    if selected_cnt == m:
        print_answer()
        return
    if num_index == n + 1:
        return

    arr[num_index] = True
    choose(num_index + 1, selected_cnt + 1)
    arr[num_index] = False

    choose(num_index + 1, selected_cnt)


choose(1, 0)