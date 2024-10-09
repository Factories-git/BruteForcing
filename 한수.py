def is_arithmetic_sequence(s):
    if len(s) < 2:
        return True
    diff = s[1] - s[0]
    for i in range(len(s) - 1):
        if s[i + 1] - s[i] != diff:
            return False
    return True


r = 0
for i in range(1,int(input())+1):
    if is_arithmetic_sequence(list(map(int,str(i)))):
        r += 1

print(r)