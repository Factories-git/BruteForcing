l = sorted([int(input()) for i in range(9)])
add = sum(l)
isfinish = False
for i in range(len(l)):
    isfinish = False
    for j in range(i+1,len(l)):
        if add - l[i] - l[j] == 100:
            l[i] = l[j] = 0
            isfinish = True
    if isfinish:
        break

for i in l:
    if i != 0:
        print(i)