import sys

input = sys.stdin.readline

time = float('inf')
n, m, b = map(int, input().split())
world = [list(map(int, input().split())) for _ in range(n)]
height = 0
for k in range(257):
    inventory = b
    new_time = 0
    for i in range(n):
        for j in range(m):
            if world[i][j] == k:
                continue
            else:
                if world[i][j] < k:
                    how_many = k - world[i][j]
                    new_time += how_many
                    inventory -= how_many
                else:
                    how_many = world[i][j] - k
                    new_time += 2 * how_many
                    inventory += how_many

    if inventory >= 0:
        if time >= new_time:
            height = k
            time = new_time
print(time, height)