minimum = int(input().strip())
maximum = int(input().strip())
sleep_hours = int(input().strip())

if sleep_hours < minimum:
    print('Deficiency')
else:
    if sleep_hours > maximum:
        print('Excess')
    else:
        print('Normal')
