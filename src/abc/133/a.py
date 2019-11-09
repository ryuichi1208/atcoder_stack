n,a,b = map(int, input().split())
ans = n * a
if ans > b:
    ans = b
print(ans)
