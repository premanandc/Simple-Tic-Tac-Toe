number_of_halls = int(input().strip())
capacity = int(input().strip())
number_of_viewers = int(input().strip())

can_accommodate = number_of_halls * capacity >= number_of_viewers
print(can_accommodate)
