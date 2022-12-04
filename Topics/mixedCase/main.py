words = input().split()
print(words[0].lower() + "".join(x.capitalize() for x in words[1:]))
