n = int(input())

arr = [0] * 2001
cur_pos = 1000

for _ in range(n):
    move_num, direction = input().split()
    move_num = int(move_num)
    if direction == 'R':
        for i in range(cur_pos, cur_pos + move_num):
            arr[i] += 1
        cur_pos += move_num
    else:
        for i in range(cur_pos, cur_pos - move_num, -1):
            arr[i] += 1
        cur_pos -= move_num

ans = 0
for j in range(len(arr)):
    if arr[j] >= 2:
        ans += 1
print(ans)