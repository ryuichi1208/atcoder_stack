n, m = list(map(int, input().split()))
l = [list(map(int, input().split())) for i in range(n)]

cnt=0

for i in range(m):
    print(i, l[0][0])
    if (i+1 == l[i][0]):
        cnt += 1
        print(str(l[i][0]).zfill(6) + str(cnt).zfill(6))

