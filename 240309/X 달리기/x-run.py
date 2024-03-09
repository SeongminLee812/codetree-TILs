x = int(input())

cur_vel = 1
cur_pos = 1
elapsed = 1

def sigma(n):
    return (n * (n + 1)) // 2

while True:
    if cur_pos + sigma(cur_vel) < x: # 속력에 1 더했을 때 넘지 않는다면
        cur_vel += 1
        cur_pos += cur_vel
        elapsed += 1
    elif cur_pos + sigma(cur_vel) == x:
        elapsed += cur_vel
        break
    elif cur_pos + sigma(cur_vel) > x: # 넘으면
        cur_vel -= 1
        cur_pos += cur_vel
        elapsed += 1

print(elapsed)