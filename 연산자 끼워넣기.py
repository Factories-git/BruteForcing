n = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
min_val = 1e9
max_val = -1e9


def dfs(i, now):
    global min_val, max_val, add, sub, mul, div
    if i == n:
        min_val = min(min_val, now)
        max_val = max(max_val, now)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + arr[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - arr[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * arr[i])
            mul += 1
        if div > 0:
            div -= 1
            if now < 0:
                dfs(i + 1, -(abs(now) // arr[i]))
            else:
                dfs(i+1, int(now // arr[i]))
            div += 1


dfs(1, arr[0])

print(max_val)
print(min_val)
