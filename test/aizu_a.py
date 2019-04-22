n = int(input())
k = int(input())
l = list(map(int, input().split()))

L=[]
for i in range(n):
    if(i == 0):
        L.append(0)
        L.append(l[i])
    else:
        L.append(L[i]+l[i])

ans=0
for i in range(n-k+1):
    tmp = L[i+k] - L[i]
    ans = max(ans, tmp)

print(ans)

