file = open('input.txt', 'r')

l1 = []
l2 = []
total = 0

for line in file:
    loc = line.split()
    l1.append(int(loc[0]))
    l2.append(int(loc[1]))

l1.sort()
l2.sort()

for i in range(len(l1)):
    dist = abs(l1[i] - l2[i])
    total = total + dist

print(total)