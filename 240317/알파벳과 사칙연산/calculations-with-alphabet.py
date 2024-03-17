import sys

formular = input()

def calc(mapping):
    val = mapping[formular[0]]
    for i in range(1, len(formular), 2):
        if formular[i] == '-':
            val -= mapping[formular[i + 1]]
        elif formular[i] == '+':
            val += mapping[formular[i + 1]]
        elif formular[i] == '*':
            val *= mapping[formular[i + 1]]
    return val

num_list = []
ans = -sys.maxsize
def choose(index):
    global ans
    if index == 7:
        mapping = dict(zip(['a', 'b', 'c' ,'d' ,'e', 'f'], num_list))
        val = calc(mapping)
        ans = max(ans, val)
        return

    for i in range(1, 5):
        num_list.append(i)
        choose(index + 1)
        num_list.pop()

choose(1)
print(ans)