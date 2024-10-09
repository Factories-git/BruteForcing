from itertools import combinations

v = {'a','e','i','o','u'}
l,c = map(int, input().split())

arr = input().split()
arr.sort()

for password in combinations(arr,l):
    c = 0
    for i in password:
        if i in v:
            c += 1
    if 1 <= c <= l-2:
        print(''.join(password))