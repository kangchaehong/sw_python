n, m = map(int,input().split())
coin = []
for i in range(n) :
    coin.append(int(input()))

d = [10001] * (m+1)
d[0] = 0

for i in coin :
    for j in range(i,m+1) :
        if j == i :
            d[j] = 1
        else :
            d[j] = min(d[j], d[j-i]+1)

if d[m] == 10001 :
    print(-1)
else :
    print(d[m])
