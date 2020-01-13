import sys

n = int(input())
s = input()

if (n%2!=0):
    print("No")
    sys.exit(0)

l = n//2
if s[:l] == s[l:]:
    print("Yes")
else:
    print("No")
