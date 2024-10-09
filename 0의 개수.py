t = int(input())
for i in range(t):
    c = 0
    n,m = map(int, input().split())
    for j in range(n, m+1):
        s = str(j)
        c += s.count('0')
    print(c)
