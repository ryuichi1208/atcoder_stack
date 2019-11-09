import sys

n = int(input())

if n <= 3:
    print(0)
    sys.exit()

if n%2==0:
    print(n//2-1)
else:
    print(n//2)
