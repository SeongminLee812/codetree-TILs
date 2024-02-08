a = input()

total = 0

for i in range(len(a) - 1):
    if a[i] == '(' and a[i + 1] == '(':
        for j in range(i + 1, len(a) - 1):
            if a[j] == ')' and a[j + 1] == ')':
                total += 1

print(total)