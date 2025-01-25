price = [12, 21, 31, 40, 49, 58, 69, 79, 90, 101]

left = 0
right = 0
min_ = float('inf')
how = [0] * 2
for i in range(10):
    while i <= right < 10:
        for j in range(10):
            print(right, j)
            pr = price[right] * j
            if pr + price[i] < min_ and right * j + i == 15:
                min_ = min(min_, pr + i)
                how[0] = price[i]
                how[1] = price[right]
        right += 1
print(min_, how)