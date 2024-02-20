def reverse_str(a: str):
    result =''
    for s in a:
        result = s + result
    return result

a = input()

if a == reverse_str(a):
    print('Yes')
else:
    print('No')