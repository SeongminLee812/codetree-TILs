import sys

arr = input()

def calc(num_list):
    alpha_list = ['a', 'b', 'c', 'd', 'e', 'f']
    alpha_dict = dict(zip(alpha_list, num_list))

    value = alpha_dict[arr[0]]

    for i in range(1, len(arr), 2):
        if arr[i] == '*':
            value *= alpha_dict[arr[i + 1]]
        elif arr[i] == '-':
            value -= alpha_dict[arr[i + 1]]
        elif arr[i] == '+':
            value += alpha_dict[arr[i + 1]]
    return value


def go(curr_index_in_ans):
    global ans
    if curr_index_in_ans == 6:
        value = calc(nums)
        ans = max(value, ans)
        return

    for i in range(1, 5):
        nums.append(i)
        go(curr_index_in_ans + 1)
        nums.pop()

ans = -sys.maxsize
nums = []

go(0)
print(ans)