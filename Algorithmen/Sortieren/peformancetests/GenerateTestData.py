from random import randint

n = 1000000
min = 0
max = n

TestData = []

for i in range(0, n):
    TestData.append(randint(min, max))

str_array = [str(x) for x in TestData]

with open(file="Algorithmen/Sortieren/peformancetests/IntSet.txt", mode='w') as f:
    f.writelines("\n".join(str_array))
