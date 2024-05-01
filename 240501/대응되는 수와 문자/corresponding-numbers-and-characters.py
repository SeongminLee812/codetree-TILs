n, m =map(int, input().split())
num_dict = dict()
str_dict = dict()

for i in range(1, n + 1):
    input_string = input()
    num_dict[i] = input_string
    str_dict[input_string] = i


for _ in range(m):
    target = input()
    if target.isalpha():
        print(str_dict[target])
    else:
        print(num_dict[int(target)])