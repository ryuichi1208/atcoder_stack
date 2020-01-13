import math
import itertools

n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

x = 0
y = 0
tmp = 0
LL = list(itertools.permutations([i for i in range(n)], n))
for i in LL:
    for j in range(2):
        if j == 0:
            x = l[i[j]][0]
            y = l[i[j]][1]
        else:
            x -= l[i[j]][0]
            y -= l[i[j]][1]

    print(x**2, y**2)
    tmp += math.sqrt(x**2 + y**2)
    y=0
    x=0

print(tmp/len(LL))
