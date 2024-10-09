n = input()
l = len(n)
n = n[:l-2]
f = int(input())
for i in range(100):
    n = n[:l-2]
    if i < 10:
        i = '0' + str(i)
    n += str(i)
    if int(n) % f == 0:
        print(i)
        break

