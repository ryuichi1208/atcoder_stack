n = int(input())


# @return [0]:約数の個数 [1]:約数リスト
def divisor(num):
    ret=[]
    L=[]
    for i in range(1,num+1):
        if (num%i==0):
            L.append(i)
    ret.append(len(L))
    ret.append(L)
    return ret


L=[]
ans=0
for i in range(1,n+1):
    if(i%2==0):
        continue
    else:
        for j in range(1,n+1):
            if(i%j==0):
                L.append(j)
    if (len(L)==8):
        ans+=1
    L.clear()

print(ans)

print(divisor(15))
