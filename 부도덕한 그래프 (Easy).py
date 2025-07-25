n, m = map(int, input().split())
graph = [set() for i in range(n+1)]
answer = 0
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].add(v)

for x in range(1, n+1):
    for y in range(x+1, n+1):
        if y in graph[x] or x in graph[y]:
            continue
        answer += len(graph[x].intersection(graph[y]))

print(answer)