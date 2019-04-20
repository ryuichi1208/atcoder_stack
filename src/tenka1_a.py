n, m,l = list(map(int, input().split()))

if (n <= l and l <= m) :
    print("Yes")
elif (m <= l and l <= n):
    print("Yes")
else :
    print("No")
