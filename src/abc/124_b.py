import sys

n=int(input())
l=list(map(int, input().split()))

ans=1
tmp=0 

for i in range(n) :
    if (i == 0):
        tmp = l[i]
        continue
       
    if (tmp <= l[i]):
        ans += 1
        tmp = l[i]

print (ans)
