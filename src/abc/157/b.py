import sys

bing = [list(map(int, input().split())) for i in range(3)]
n = int(input())
line = [int(input()) for i in range(n)]

ans = [[0,0,0], [0,0,0], [0,0,0]]
for l in line:
    for i in range(3):
        for j in range(3):
            if l == bing[i][j]:
                ans[i][j] = bing[i][j]

# 横比較
for l in ans:
    if 0 not in l:
        print("Yes")
        sys.exit()

# 縦比較
for i in range(3):
    if ans[0][i] != 0 and ans[1][i] != 0 and ans[2][i] != 0:
        print("Yes")
        sys.exit()

# 斜め比較
if ans[0][0] != 0 and ans[1][1] != 0 and ans[2][2] != 0:
    print("Yes")
elif ans[0][2] != 0 and ans[1][1] != 0 and ans[2][0] != 0:
    print("Yes")
else:
    print("No")

