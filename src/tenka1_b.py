n = int(input())
s = input()
k = int(input())

c = s[k-1]

L=[]
for i in range(len(s)):
    if(s[i] != c):
        L.append("*")
        continue
    else:
        L.append(s[i])

st = ''.join(L)
print(st)

