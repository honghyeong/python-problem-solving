import itertools

numbers="17"
permute=set(map(''.join,itertools.permutations(list(numbers),1)))
print(permute)