from itertools import combinations

house, chicken = [], []
n, m = map(int, input().split())
for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))
        elif data[c] == 2:
            chicken.append((r, c))

candiates = list(combinations(chicken, m))


def get_(candiate):
    re = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candiate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        re += temp
    return re


result = 1e9
for candiate in candiates:
    result = min(result, get_(candiate))

print(result)
