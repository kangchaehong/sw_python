n = int(input())
t, p = [], []
for i in range(n) :
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

d = [0]*(n+1)
mv = 0
for i in range(n-1, -1, -1) :
    time = t[i] + i
    if time > n :
        d[i] = mv
    else :
        d[i] = max(p[i]+d[time], mv)
        mv = d[i]
print(max(d))