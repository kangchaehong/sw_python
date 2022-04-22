# 입력부
t = int(input())
result = []
for _ in range(t):
    dp = []
    maxv = 0
    n, m = map(int, input().split())
    dplist = list(map(int, input().split()))
    for i in range(n) :
        dp.append(dplist[i*m:(i*m)+m])
    for j in range(1, m):
        for i in range(n):
            if i - 1 >= 0 and j - 1 >= 0:
                left_down = dp[i - 1][j - 1]
            else:
                left_down = -1
            if i+1 < n and j-1 >=0:
                right_up = dp[i+1][j-1]
            else :
                right_up = -1
            left = dp[i][j - 1]

            dp[i][j] = dp[i][j] + max(left, left_down, right_up)
    for i in range(n):
        maxv = max(maxv, dp[i][m - 1])
    result.append(maxv)

for i in result :
    print(i)
