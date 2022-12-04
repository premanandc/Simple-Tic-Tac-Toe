height = int(input())

for i in range(1, height + 1):
    print(('#' * (i * 2 - 1)).center(height * 2 - 1))
