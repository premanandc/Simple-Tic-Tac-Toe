words = input().strip().split()
s_words = [word for word in words if word[-1] == 's']
print('_'.join(s_words))
