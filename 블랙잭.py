n,m = map(int, input().split())
cards = list(map(int, input().split()))
max_ = 0
for i in range(len(cards)):
    for j in range(len(cards)):
        if i == j:
            continue
        for k in range(len(cards)):
            if i == k or j == k:
                continue
            card = cards[i] + cards[j] + cards[k]
            if card <= m:
                if abs(m-card) < abs(m-max_):
                    max_ = card
print(max_)