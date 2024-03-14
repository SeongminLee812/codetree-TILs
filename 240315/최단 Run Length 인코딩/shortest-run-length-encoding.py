# 오른쪽으로 적절히 shifting
# 문자열의 길이는 10임. 즉 10번 shifting 해서 길이를 구하고 가장 짧은 것을 출력하면 됨.
from collections import defaultdict

def shift(string: str, iterations: int):
    string_list = list(string)

    for _ in range(iterations):
        temp = string_list[-1]
        for i in range(len(string_list) - 1, 0, -1):
            string_list[i] = string_list[i - 1]
        string_list[0] = temp

    return ''.join(string_list)

def encode(string):
    result = ''

    cnt = 1
    for i in range(len(string)):
        if i == len(string) - 1:
            result += string[i]
            result += str(cnt)

        elif string[i] != string[i + 1]:
            result += string[i]
            result += str(cnt)
            cnt = 1
        elif string[i] == string[i + 1]:
            cnt += 1

    return result

ans = 21

a = input()
for i in range(1, len(a) + 1):
    shifted_string = shift(a, i)
    encoded_string = encode(shifted_string)
    ans = min(ans, len(encoded_string))

print(ans)