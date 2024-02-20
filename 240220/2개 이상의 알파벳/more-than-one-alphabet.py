def is_all_same(text: str):
    if len(text) == 1:
        return True
    for i in range(len(text) - 1):
        if text[i] != text[i + 1]:
            return False
    return True

a = input()
if is_all_same(a):
    print('No')
else:
    print('Yes')