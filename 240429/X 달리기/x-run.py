x = int(input())

left_distance = x
v = 1

t = 0

def pred_distance(velocity):

    return (velocity * (velocity + 1)) // 2

while left_distance:
    t += 1
    left_distance -= v
    if left_distance == 0:
        break


    if pred_distance(v + 1) <= left_distance:
        v += 1
    elif pred_distance(v) <= left_distance:
        v = v
    else:
        v -= 1


print(t)