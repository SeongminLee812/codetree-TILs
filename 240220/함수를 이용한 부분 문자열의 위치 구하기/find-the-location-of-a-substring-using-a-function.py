a = input()
target = input()

def find_position():
    a_len = len(a)
    target_len = len(target)

    for i in range(a_len - target_len + 1) :
        if a[i:i + target_len] == target:
            return i
    return -1

print(find_position())