import sys

x = int(input())

if x == 1:
    print(1)
    sys.exit()

prev_vel = 1
cur_pos = 0
elapsed = 0

go_on = True

def sigma(n):
    return (n * (n + 1)) // 2

while True:
    if cur_pos == x:
        break
    cur_pos += prev_vel
    if go_on and cur_pos + sigma(prev_vel + 1) <= x:
        cur_vel = prev_vel + 1

    # 한번이라도 넘어버리면 그 이후에는 감소 or 유지 밖에 없음
    # 넘는 경우
    if cur_pos + sigma(cur_vel) > x:
        go_on = False
        cur_vel = prev_vel - 1

    # 유지하는 경우
    elapsed += 1
    prev_vel = cur_vel

print(elapsed)