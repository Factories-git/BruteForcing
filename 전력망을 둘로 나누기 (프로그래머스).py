def solution(n, wires):
    g = [[] for _ in range(n + 1)]
    for a, b in wires:
        g[a].append(b)
        g[b].append(a)

    def dfs(g, start):
        count = 1
        visit.add(start)
        for node in g[start]:
            if node not in visit:
                count += dfs(g, node)
        return count

    answer = 9999999
    for a, b in wires:
        re = []
        g[a].remove(b)
        g[b].remove(a)
        visit = set()
        for i in range(1, n+1):
            if i not in visit:
                re.append(dfs(g, i))
        g[a].append(b)
        g[b].append(a)
        if len(re) == 1:
            continue
        answer = min(answer, abs(re[0] - re[1]))
    return answer

