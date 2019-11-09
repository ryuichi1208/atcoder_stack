n, m = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]

L = [i**2 for i in range(30)]
ans=0
tmp=0
z = []
for i in range(n):
    for j in range(n-1):
        ai = i
        aj = j
        if ai > aj:
            t = ai
            ai = aj
            aj = t
        if [ai, aj] in z:
            continue
        if ai == aj :
            continue
        for k in range(m):
            su = l[i][k] - l[j+1][k]
            su = abs(su)**2
            tmp += su
        if tmp in L:
            ans+=1
        tmp=0
        z.append([ai,aj])

print(ans)
