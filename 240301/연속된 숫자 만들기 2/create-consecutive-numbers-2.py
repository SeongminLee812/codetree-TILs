a, b, c = map(int, input().split())

# 셋 다 떨어진 경우
# if (abs(a - b) > 1) and (abs(b - c) > 1):
#     print(2)
# 셋 다 붙은 경우
if (abs(a - b) == 1) and (abs(b - c) == 1):
    print(0)
else:
    print(2)