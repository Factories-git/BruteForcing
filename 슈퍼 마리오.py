target = 100
add = 0
i = 0
for i in range(10):
    ipt = int(input())
    add += ipt
    if add >= target:
        print(add)
        break