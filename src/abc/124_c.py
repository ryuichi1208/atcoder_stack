import sys

s=input()
l=len(s)

#cnt0=s.count("0")
#cnt1=s.count("1")
#print (cnt0, cnt1)

p1=0
p2=0

for i in range(l):
    if (i%2==0):
        if(s[i] == "0"):
            p1+=1
    else:
        if(s[i] != "0"):
            p1+=1

for i in range(l):
    if (i%2!=0):
        if(s[i] == "0"):
            p2+=1
    else:
        if(s[i] != "0"):
            p2+=1

print (min(p1, p2))
