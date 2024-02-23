start_day, start_h, start_m = 11, 11, 11
end_day, end_h, end_m = map(int, input().split())

end_minute = (end_day * 24 * 60 )+ (end_h * 60) + end_m
start_minute = (start_day * 24 * 60) + (start_h * 60) + start_m

elapsed_minute = end_minute - start_minute

if elapsed_minute < 0:
    print(-1)
else:
    print(elapsed_minute)