file = open('input.txt', 'r')

l1 = []
l2 = []
score = 0

for line in file:
    loc = line.split()
    l1.append(int(loc[0]))
    l2.append(int(loc[1]))

l1.sort()
l2.sort()

for i in range(len(l1)):
    count = 0
    for j in range(len(l2)):
        if l1[i] == l2[j]:
            count += 1

    score += count * l1[i]


print(score)
