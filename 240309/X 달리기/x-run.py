x = int(input())
t = 0
left_dist = x
v = 1

while True:
    left_dist -= v
    t += 1
    if left_dist == 0:
        break

    # 속도를 증가시킬 경우 이동거리
    if left_dist >= (v + 1) * (v + 2) // 2:
        v += 1

    # 속도를 유지할 경우 이동거리 고려
    elif left_dist >= v * (v + 1) // 2:
        v = v

    # 속도를 증가시키거나 유지하면 target을 넘어가버리는 경우 속도를 줄여야함.
    else:
        v -= 1

print(t)