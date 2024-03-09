x = int(input())

cur_vel = 1
cur_pos = 0
elapsed = 0

def sigma(n):
    return (n * (n + 1)) // 2

while True:
    elapsed += 1
    if cur_pos + sigma(cur_vel) < x:
        cur_pos += cur_vel
        cur_vel += 1
    else:
        cur_vel -= 1
        elapsed -= 1
        break

while cur_vel > 1:
    elapsed += 1
    cur_vel -= 1
    cur_pos += cur_vel

elapsed += x - cur_pos # 속력 1 로 나머지 구간 이동

print(elapsed)