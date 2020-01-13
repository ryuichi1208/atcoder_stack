n, m = map(int,input().split())
a = [input().split() for i in range(m)]
p = [int(i[0]) for i in a]
q = [j[1] for j in a]
 
ac = 0
wa = 0
wa_c = [0] * n
ac_c = [False] * n
 
for t in range(m):
    if ac_c[p[t]-1]:
        continue
    if q[t] == 'AC':
        ac += 1
        ac_c[p[t]-1] = True
        wa += wa_c[p[t]-1]
    else:
        wa_c[p[t]-1] += 1
print(ac,wa)
