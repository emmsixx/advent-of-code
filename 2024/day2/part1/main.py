file = open('input.txt', 'r')

unsafe = 0
lc = 0

for line in file:
    x = line.split()
    lc += 1
    sum = 0
    for y in range(len(x) - 1):
        diff = int(x[y + 1]) - int(x[y])
        if abs(diff) > 3 or abs(diff) < 1 or (sum < 0 and sum + diff > sum) or (sum > 0 and sum + diff < sum):
            unsafe += 1
            break
        sum += diff

print(lc-unsafe)
