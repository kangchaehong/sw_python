n, m = map(int,input().split())
coins = []
for i in range(n) :
    coins.append(int(input()))
d = [10001] * (m+1)
d[0] = 0
for coin in coins :
    for i in range(coin, m+1) :
        d[i] = min(d[i], d[i - coin] + 1)
if d[m] != 10001 :
    print(d[m])
else :
    print(-1)