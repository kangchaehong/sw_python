a = input()
b = input()
alen = len(a)
blen = len(b)

dp = [[0]*(blen+1) for _ in range(alen+1)]
for i in range(alen+1) :
    dp[i][0] = i
for i in range(0,blen+1) :
    dp[0][i] = i

for i in range(alen) :
    for j in range(blen) :
        if a[i] == b[j] :
            dp[i+1][j+1] = dp[i][j]
        else :
            dp[i+1][j+1] = 1+min(dp[i][j], dp[i+1][j], dp[i][j+1])
print(dp[alen][blen])