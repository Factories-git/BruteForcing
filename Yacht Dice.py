pedigree = input()
d1, d2, d3 = map(int, input().split())
score = 0
new_score = 0
for d4 in range(1, 7):
    for d5 in range(1, 7):
        new_score = 0
        if pedigree[10] == 'Y':
            if d1 == d2 == d3:
                if d4 == d5 == d1:
                    new_score = 50

        if pedigree[6] == 'Y':
            if d1 == d2 or d1 == d3:
                if d4 == d5 == d1:
                    new_score = max(new_score, d1 * 4)

            if d2 == d3:
                if d4 == d5 == d2:
                    new_score = max(new_score, d2 * 4)

        if pedigree[8] == 'Y':
            if {d1, d2, d3, d4, d5} == {1, 2, 3, 4, 5}:
                new_score = max(new_score, 30)

        if pedigree[9] == 'Y':
            if {d1, d2, d3, d4, d5} == {2, 3, 4, 5, 6}:
                new_score = max(new_score, 30)

        if pedigree[7] == 'Y':
            flag = True
            full_house = {d1, d2, d3, d4, d5}
            if len(full_house) == 2:
                for j in full_house:
                    if [d1, d2, d3, d4, d5].count(j) == 1:
                        flag = False
                        break
                if flag:
                    new_score = max(d1 + d2 + d3 + d4 + d5, new_score)

        if pedigree[11] == 'Y':
            new_score = max(new_score, d1 + d2 + d3 + d4 + d5)

        for i in range(6):
            if pedigree[i] == 'Y':
                new_score = max(new_score, [d1, d2, d3, d4, d5].count(i + 1) * (i + 1))
        score = max(new_score, score)
print(score)
