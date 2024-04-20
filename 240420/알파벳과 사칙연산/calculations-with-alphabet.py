import sys

equation = input()
ans = -sys.maxsize

def calc(num_list):
    num_dict = dict(zip(['a', 'b', 'c', 'd', 'e', 'f'], num_list))
    result = num_dict[equation[0]]
    for i in range(1, len(equation), 2):
        if equation[i] == '-':
            result -= num_dict[equation[i + 1]]
        elif equation[i] == '*':
            result *= num_dict[equation[i + 1]]
        elif equation[i] == '+':
            result += num_dict[equation[i + 1]]
    return result


def go(select_index):
    global ans
    if select_index == 7:
        ans = max(ans, calc(selected))
        return

    for i in range(1, 5):
        selected.append(i)
        go(select_index + 1)
        selected.pop()

selected = []
go(1)
print(ans)