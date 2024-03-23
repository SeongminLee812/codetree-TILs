n, m = map(int, input().split())

ans = [0] * (n + 1)

def choose(curr_index, cnt):
    """
    1 ~ n 까지 숫자를 뽑을 지 말지 결정하는 함수.
    뽑은 숫자가 m개라면 출력
    curr_index 번째 숫자를 뽑을 지 말지 결정하고,
    숫자를 몇개 뽑았는 지에 대한 정보 cnt를 넘겨줌
    :param curr_index:
    :return:
    """
    if curr_index == n + 1:
        if cnt == m:
            for i in range(1, n + 1):
                if ans[i]:
                    print(i, end=' ')
            print()
        return

    ans[curr_index] = 1
    choose(curr_index + 1, cnt + 1)
    ans[curr_index] = 0

    choose(curr_index + 1, cnt)

choose(1, 0)