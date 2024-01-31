month_dict = {1: 31, 2: 28, 3: 31,
              4: 30, 5: 31, 6: 30,
              7: 31, 8: 31, 9: 30,
              10: 31, 11: 30, 12: 31}

yoon = False

y, m, d = map(int, input().split())

if y % 400 == 0:
    yoon = True
elif y % 100 == 0:
    yoon = False
elif y % 4 == 0:
    yoon = True

if yoon:
    month_dict[2] += 1

if d > month_dict[m]:
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