import sys

MAX_INT = 1000
t, a, b = map(int, input().split())
arr = [0] * (MAX_INT + 1)

for _ in range(t):
    char, position = input().split()
    position = int(position)
    arr[position] = char

def in_range(index):
    return index >= 0 and index <= MAX_INT + 1

# index를 기준으로 작아지는 방향 (s를 만나거나, in range에서 벗어나면 종료)
# index를 기준으로 커지는 방향 (s를 만나거나, in range에서 벗어나면 종료)
def shortest_s(index):
    left = sys.maxsize
    right = sys.maxsize

    for i in range(index, 0, -1):
        if arr[i] == 'S':
            left = index - i
            break
    for i in range(index, MAX_INT + 1):
        if arr[i] == 'S':
            right = i - index
            break
    return min([left, right])

def shortest_n(index):
    left = sys.maxsize
    right = sys.maxsize

    for i in range(index, 0, -1):
        if arr[i] == 'N':
            left = index - i
            break
    for i in range(index, MAX_INT + 1):
        if arr[i] == 'N':
            right = i - index
            break
    return min([left, right])

special_position = 0
for x in range(a, b + 1):
    if shortest_s(x) <= shortest_n(x):
        special_position += 1

print(special_position)