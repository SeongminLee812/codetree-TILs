a, b, c = map(int, input().split())

# 셋 중 두개가 한칸만 떨어진 경우
if (abs(a - b) == 2) or (abs(b - c) == 2):
    print(1)
# 셋 다 붙은 경우
elif (abs(a - b) == 1) and (abs(b - c) == 1):
    print(0)
else:
    print(2)