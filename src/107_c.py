import sys

n, m = list(map(int, input().split()))
l = list(map(int, input().split()))

if(m==1):
    print(l[0])
    sys.exit()

l.append(0)
l.sort()
ind=l.index(0)

p1=9999999
p2=9999999
p3=9999999

if(m <= n-ind):
    p1 = l[ind+m]
if(m <= ind):
    p2 = l[ind-m]




print(min(p1,p2,p3))
