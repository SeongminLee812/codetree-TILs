a = input()
b = input()

ASCII_NUM = [0] * 128

for s in a:
    ASCII_NUM[ord(s)] += 1

for s in b:
    ASCII_NUM[ord(s)] -= 1

ok = True
for i in range(len(ASCII_NUM)):
    if ASCII_NUM[i] != 0:
        print('No')
        ok = False
        break
if ok:
    print('Yes')