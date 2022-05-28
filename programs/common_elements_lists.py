n1 = [11,22,33,44,55]
n2 = [66,88,22,33,99]
# filter(function, sequence)
intersection = filter(lambda n : n in n2, n1)
print(list(intersection))

'''
output:
[22, 33]
'''
