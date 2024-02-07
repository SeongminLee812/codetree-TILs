arr = list(input())

total = 0

for i in range(len(arr)):
    if arr[i] == '(':
        for j in range(i, len(arr)):
            if arr[j] == ')':
                total += 1

print(total)