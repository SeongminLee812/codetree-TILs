l, r = input().split()
arr = list(input())

left = [
    ['q', 'w', 'e', 'r', 't'],
    ['a', 's', 'd', 'f', 'g'],
    ['z', 'x', 'c', 'v', '-']
]

right = [
    ['-', 'y', 'u', 'i', 'o', 'p'],
    ['-', 'h', 'j', 'k', 'l'],
    ['b', 'n', 'm']
]

left_x, left_y = -1, -1
for i in range(3):
    if l in left[i]:
        left_x = i
        for j in range(len(left[i])):
            if l == left[i][j]:
                left_y = j

right_x, right_y = -1, -1
for i in range(3):
    if r in right[i]:
        right_x = i
        for j in range(len(right[i])):
            if r == right[i][j]:
                right_y = j

elapsed_time = 0

for s in arr:
    for i in range(3):
        if s in left[i]:
            elapsed_time += abs(i - left_x)
            left_x = i
            for j in range(len(left[i])):
                if s == left[i][j]:
                    elapsed_time += abs(j - left_y)
                    left_y = j
        elif s in right[i]:
            elapsed_time += abs(i - right_x)
            right_x = i
            for j in range(len(right[i])):
                if s == right[i][j]:
                    elapsed_time += abs(j - right_y)
                    right_y = j

    elapsed_time += 1

print(elapsed_time)