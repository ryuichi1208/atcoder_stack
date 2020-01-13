n, m = list(map(int, input().split()))
l = [int(input()) for i in range(n)]
l.sort()

min_n=10000000
tmp=0

for i in range(n-m+1):
    tmp = l[i+m-1] - l[i]
    if (tmp < min_n):
      min_n = tmp

print(min_n)
