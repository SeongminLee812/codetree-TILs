equation = input()

def calc(num_list):
    num_dict = dict(zip(['a', 'b', 'c', 'd', 'e', 'f'], num_list))
    ans = num_dict[equation[0]]
    for i in range(1, len(equation), 2):
        if equation[i] == '-':
            ans -= num_dict[equation[i + 1]]
        elif equation[i] == '*':
            ans *= num_dict[equation[i + 1]]
        elif equation[i] == '+':
            ans += num_dict[equation[i + 1]]
    return ans



def go(select_index):
    global result
    if select_index == 7:
        result = max(result, calc(selected))
        return

    for i in range(1, 5):
        selected.append(i)
        go(select_index + 1)
        selected.pop()

result = 0
selected = []
go(1)
print(result)