n = int(input())
cnt = 0
for i in range(1,n+1):
    j = str(i)
    j = list(map(int, j))
    s = sum(j)
    if i % s == 0:
        cnt += 1
print(cnt)