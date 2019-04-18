n, k = list(map(int, input().split()))
ans = (n//k)**3
if(k%2==0):
    n-=k//2
    ans+=(n//k+1)**3
print(ans)
