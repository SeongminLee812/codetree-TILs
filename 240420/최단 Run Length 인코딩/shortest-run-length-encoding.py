a = input()

def run_length(strings):
    result = ""
    repeat = 1
    if len(strings) == 1:
        return 2
    for i in range(1, len(strings)):
        if strings[i - 1] != strings[i]:
            result += strings[i - 1]
            result += str(repeat)
            repeat = 1
        else:
            repeat += 1
        if i == len(strings) - 1:
            result += strings[i]
            result += str(repeat)

    return len(result)

ans = 100
for _ in range(len(a) + 1):
    ans = min(ans, run_length(''.join(a)))
    a = list(a)
    temp = a[-1]
    for i in range(len(a) - 1, 0, -1):
        a[i] = a[i - 1]
    a[0] = temp

print(ans)