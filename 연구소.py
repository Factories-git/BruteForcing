n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
 def backtracking(count, graph_):
     if count == 3:
         return
     is_ = True
     for i in range(n):
         for j in range(m):
             if count == 3:
                 is_ = False
                 break
             graph_[i][j] = 1
         if not is_:
            break
     return graph_
