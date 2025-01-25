n, d, k, c = map(int, input().split())
sushi_belt = [int(input()) for i in range(n)]
is_c = c in sushi_belt

re = 0
for i in range(n):
    window = [sushi_belt[(j + i) % n] for j in range(k)]
    sushi_type = window.copy()

    sushi_type.append(sushi_belt[(i - 1) % n])
    if len(window) >= k and sushi_type[-1] == c:
        re = max(re, len(set(sushi_type)))
    sushi_type.pop()

    sushi_type.append(sushi_belt[(i + 1) % n])
    if len(window) >= k and sushi_type[-1] == c:
        re = max(re, len(set(sushi_type)))
    sushi_type.pop()

    sushi_type.append(c)

    if len(window) >= k:
        re = max(re, len(set(sushi_type)))

print(re)

"""
중요 반례:
8 30 4 30
7
7
3
7
7
8
7
7

답:4
내 답: 5
"""
