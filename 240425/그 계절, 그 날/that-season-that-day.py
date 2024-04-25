y, m, d = map(int, input().split())

month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
yoon = False

if y % 400 == 0:
    yoon = True
elif y % 100 == 0:
    yoon = False
elif y % 4 == 0:
    yoon = True

if yoon:
    month[2] += 1


if d > month[m]:
    print(-1)
else:
    if 3 <= m <= 5:
        print('Spring')
    elif 6 <= m <= 8:
        print('Summer')
    elif 9 <= m <= 11:
        print('Fall')
    else:
        print('Winter')