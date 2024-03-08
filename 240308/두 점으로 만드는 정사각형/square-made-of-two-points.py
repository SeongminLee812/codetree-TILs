height_list = []
width_list = []

for _ in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    width_list.append(x1)
    width_list.append(x2)
    height_list.append(y1)
    height_list.append(y2)

width = max(width_list) - min(width_list)
height = max(height_list) - min(height_list)

length = max(width, height)
print(length * length)