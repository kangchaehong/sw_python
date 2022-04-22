n = int(input())
time = []
pay =[]
dp = [0]*(n+1)
for i in range(n) :
    t, p = map(int,input().split())
    time.append(t)
    pay.append(p)

for i in range(n-1,-1,-1) :
    if time[i] + i <= n :
        dp[i] = max(dp[time[i]+i]+pay[i], dp[i+1])
    else :
        dp[i] = dp[i+1]
print(max(dp))