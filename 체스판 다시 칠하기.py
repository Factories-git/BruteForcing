bw_chess = []
wb_chess = []
is_ = True
for i in range(8):
    bw_chess.append('BW'*4 if is_ else 'WB'*4)
    wb_chess.append('WB'*4 if is_ else 'BW'*4)
    is_ = not is_
n,m = map(int, input().split())
chess = []
for i in range(n):
    chess.append(input())
min_val = n*m
for y in range(n-8+1):
    for x in range(m-8+1):
        bw = wb = 0
        for i in range(8):
            for j in range(8):
                if chess[y+i][x+j] != bw_chess[i][j]:
                    bw += 1
                elif chess[y+i][x+j] != wb_chess[i][j]:
                    wb += 1
        min_val = min(bw,wb,min_val)
print(min_val)