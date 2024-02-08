a = list(input())

alt = {'1': '0', '0': '1'}

result = 0

for i in range(len(a)):
    before = a[i]
    a[i] = alt[a[i]]
    string = ''.join(a)
    result = max(result, int(string, 2))
    a[i] = before

print(result)