n, d, k, c = map(int, input().split())
sushi_belt = [int(input()) for i in range(n)]
Check = {i: 0 for i in sushi_belt}
re = 0
for i in range(n):
    window = [sushi_belt[(j + i) % n] for j in range(k)]
    if list(dict.fromkeys(window)) != window:
        continue
    print(window)
    window.append(sushi_belt[(i - k - 1) % n])
    if list(dict.fromkeys(window)) == window and window[-1] == c:
        re = max(re, len(window))
    window.pop()
    window.append(sushi_belt[(i + 1) % n])
    if list(dict.fromkeys(window)) == window and window[-1] == c:
        re = max(re, len(window))
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
