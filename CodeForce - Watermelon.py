import math


n = int(input())


def iseven(n2):
    if n2 % 2 == 0:
        return True
    return False


if iseven(math.ceil(n / 2)):
    print('YES')
else:
    print('NO')
