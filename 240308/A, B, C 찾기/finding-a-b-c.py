# sort부터 하기

arr = list(map(int, input().split()))
arr.sort()

a_b_c = arr[-1]
a = arr[0]
b = arr[1]
c = a_b_c - a - b

print(a, b, c)