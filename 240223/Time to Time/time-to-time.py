start_h, start_m, end_h, end_m = map(int, input().split())

ans = (end_h * 60 + end_m) - (start_h * 60 + start_m)
print(ans)