n,k, m = map(int, input().split())
l = list(map(int, input().split()))

s = sum(l)
ans = n*m-s
if k < ans:
    print(-1)
elif ans <= 0:
    print(0)
else:
    print(ans)

