word_a = input()
word_b = input()

if sorted(list(word_a)) == sorted(list(word_b)):
    print('Yes')
else:
    print('No')