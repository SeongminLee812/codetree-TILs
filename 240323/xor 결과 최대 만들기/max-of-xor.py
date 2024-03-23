n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = []
max_xor = 0

def calc_xor():
    value = 0
    for i in range(m):
        value = value ^ ans[i]
    return value

def choose(curr_index, start_num):
    """
    직전의 선택한 숫자 last_num을 인자로 받아 curr_index번째 숫자를 선택하는 함수
    :param curr_index:
    :param last_num:
    :return:
    """
    global max_xor

    if curr_index == m + 1:
        val = calc_xor()
        max_xor = max(max_xor, val)
        return

    for i in range(start_num, n):
        ans.append(arr[i])
        choose(curr_index + 1, i + 1)
        ans.pop()

choose(1, 0)
print(max_xor)