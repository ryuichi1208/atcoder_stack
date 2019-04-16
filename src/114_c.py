import sys
import re

s = input()
n = int(s)

if (n < 357):
    print(0)
    sys.exit()
elif (n >= 777777753):
    print(26484)
    sys.exit()
elif (n == 357):
    print (1)
    sys.exit()

cnt=0

pattern = '^(?=.*?3)(?=.*?5)(?=.*?7)(?!.*[1246890]).*$'
repat = re.compile(pattern)

for i in range(357, n):
    res = repat.match(str(i))
    if (res):
        cnt+=1

print(cnt)
