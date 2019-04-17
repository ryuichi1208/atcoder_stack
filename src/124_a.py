n, m = list(map(int, input().split()))
ans=0
for i in range(2):
    if(n > m):
        ans += n
        n-=1
    else:
        ans+=m
        m-=1

print(ans)
