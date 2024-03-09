n = int(input())
blocks = [
    int(input())
    for _ in range(n)
]

target_num = sum(blocks) // len(blocks)

move_blocks = 0
for i in range(n):
    if blocks[i] > target_num:
        move_blocks += blocks[i] - target_num

print(move_blocks)