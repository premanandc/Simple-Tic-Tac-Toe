# put your python code here
year = int(input().strip())

if year % 100 == 0 and year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
    print('Leap')
else:
    print('Ordinary')
