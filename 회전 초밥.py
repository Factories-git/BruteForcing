n, d, k, c = map(int, input().split())
sushi_belt = [int(input()) for i in range(n)]

re = k
if c not in sushi_belt:
    re += 1
window = sushi_belt[:k]
for i in range(k, n+1):
    window = sushi_belt[i-k:i]
    if list(dict.fromkeys(window)) != window:
        continue
    window.append(sushi_belt[(i-k-1) % n])
    if list(dict.fromkeys(window)) == window and window[-1] == c:
        re = max(re, len(window))
    window.pop()
    window.append(sushi_belt[(i+1) % n])
    if list(dict.fromkeys(window)) == window and window[-1] == c:
        re = max(re, len(window))
print(re)