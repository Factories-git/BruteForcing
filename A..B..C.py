s = input()
n = len(s)
c = 0
for i in range(n):
    for j in range(i, n):
        for k in range(j, n):
            if j-i != k-j:
                continue
            if s[i] == 'A' and s[j] == 'B' and s[k] == 'C':
                c += 1
print(c)