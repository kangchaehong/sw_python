n = int(input())
array = list(map(int, input().split()))
# 순서 뒤집어서 LIS 문제로 변환
array.reverse()

dp = [1] * n

for i in range(1,n) :
    for j in range(0, i) :
        if array[j] < array[i] :
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))
