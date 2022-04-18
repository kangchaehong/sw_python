n = int(input())
time = []
pay = []
d = [0] * (n+1)
for i in range(n) :
    t,p = map(int, input().split())
    time.append(t)
    pay.append(p)

mv = 0
for i in range(n-1,-1,-1) :
    if time[i] + i > n :
        d[i] = mv
    else :
        # d[i] = max(d[time[i]+i]+pay[i], d[i+1])
        d[i] = max(d[time[i]+i]+pay[i], mv)
        mv = d[i]
print(d[0])