n = int(input())
targets = list(map(int, input().split()))
ans = []

total = 0

def check(numbers):
    for i in range(3):
        if abs(numbers[i] - targets[i]) <= 2:
            return True
    return False

def choose(num_index):
    global total
    if num_index == 3:
        if check(ans):
            total += 1
        return

    for i in range(1, n + 1):
        ans.append(i)
        choose(num_index + 1)
        ans.pop()

choose(0)
print(total)