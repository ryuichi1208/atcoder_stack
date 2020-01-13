import sys

n, m = map(int, input().split())
l = [input() for i in range(n)]

L=[]
for i in range(n):
    if (l[i].count(".") == m): 
        continue
    L.append(l[i])

flg=0
M=[]
for i in range(m):
    for j in range(len(L)):
        if(L[j][i] == "."):
            continue
        else:
            flg=1
            break
    if (flg==0):
        M.append(i)

    flg=0

M=list(set(M))

if(len(M) == 0):
    for i in range(len(L)):
        print(L[i])

    sys.exit()

ans=[]
for i in range(len(L)):
    for j in range(m):
        if j in M:
            continue
        else:
            ans.append(L[i][j])

    tmp=''.join(ans)
    print(tmp)
    ans=[]
    tmp=""

