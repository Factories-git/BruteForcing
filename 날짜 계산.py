modulo = [15, 28, 19]
goal = list(map(int, input().split()))
for i in range(3):
    goal[i] %= modulo[i]
year = [0, 0, 0]
time = 0
while True:
    time += 1
    for i in range(3):
        year[i] = (year[i] + 1) % modulo[i]
    if year == goal:
        print(time)
        break
