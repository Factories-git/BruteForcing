from itertools import permutations

rome = ['I','V','X','L']
n = int(input())
print(len(list(permutations(rome,n))))