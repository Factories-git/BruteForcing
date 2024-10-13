import math

gcd_val, lcm = map(int, input().split())
m = gcd_val * lcm
for i in range(int(math.sqrt(m)), 1, -1):
    if m % i == 0:
        if math.gcd(i, m//i) == gcd_val:
            print(i, m//i)
            break
