import math
from functools import reduce

n, m = list(map(int, input().split()))
l = list(map(int, input().split()))

l.sort()
L=[]

for i in range(n -1):
    L.append(l[i+1] - l[i])

ans = reduce(math.gcd, L)
print(ans)
