import sys

n = int(input())
arr = list(map(int, input().split()))

total = sum(arr)
group = []
ans = sys.maxsize

def choose(num_index, cnt, group_a):
    """
    현재까지 cnt개를 선택했을 때, arr에서 num_index 번째 숫자를 선택할 지 선택하지 않을 지 결정하는 함수
    :param num_index:
    :param cnt:
    :return:
    """
    global ans
    if cnt == n:
        group_b = total - group_a
        diff = abs(group_b - group_a)
        ans = min(ans, diff)
        return
    if num_index == n * 2:
        return

    # 선택
    choose(num_index + 1, cnt + 1, group_a + arr[num_index])
    # 미선택
    choose(num_index + 1, cnt, group_a)

choose(0, 0, 0)
print(ans)