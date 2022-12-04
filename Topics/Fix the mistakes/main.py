text = input()
website_addresses = ['https://', 'http://', 'www.']
words = text.split()
for word in words:
    for prefix in website_addresses:
        if word.lower().startswith(prefix):
            print(word)