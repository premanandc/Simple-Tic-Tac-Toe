# put your python code here
sequence, number = input().strip().split(' '), input().strip()
indexes = [str(x) for x in range(len(sequence)) if sequence[x] == number]
print(' '.join(indexes) if len(indexes) else 'not found')
