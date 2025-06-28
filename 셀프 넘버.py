self_nums = [i for i in range(1, 10001)]
self_nums = set(self_nums)
for i in range(1, 10001):
    k = i + sum(list(map(int, str(i))))
    if k > 10000:
        continue
    if k in self_nums:
        self_nums.remove(k)
for i in self_nums:
    print(i)