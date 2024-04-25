a, b = map(int, input().split())
n = input()

transformed = 0
now_mul = 1
for i in range(len(n) - 1, -1, -1):
    transformed += int(n[i]) * now_mul
    now_mul *= a


first_ans = []
while transformed >= b:
    transformed, mod = divmod(transformed, b)
    first_ans.append(mod)
if transformed:
    first_ans.append(transformed)

print(''.join(map(str, first_ans[::-1])))