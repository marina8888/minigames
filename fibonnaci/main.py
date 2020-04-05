# fibonnaci sequence is sum of 2 previous numbers, where first two are 1, 1...
# call a function that adds list(i-1) + list (i-2) and write it to list(i)

seq = [1,1]
# target is the xth number of fibonacci - number of elements
target = 5

for i in range(2, target + 1, 1):
    seq.append(seq[i - 1] + seq[i - 2])

print(seq[target])


