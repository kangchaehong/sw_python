n, m = map(int,input().split())
chicken = []

home_idx = []
chic_idx = []

b = []
answer = 0

for i in range(n) :
    chicken.append(list(map(int, input().split())))
    if 1 in chicken[i] :
        h = [h for h, value in enumerate(chicken[i]) if value == 1]
        for j in range(len(h)) :
            home_idx.append([i, h[j]])

    if 2 in chicken[i] :
        c = [c for c, value in enumerate(chicken[i]) if value == 2]
        for j in range(len(c)):
            chic_idx.append([i, c[j]])

cal =[[0] * len(chic_idx) for _ in range(len(home_idx))]
hap = [0] * len(chic_idx)

for i in range(len(home_idx)) :
    for j in range(len(chic_idx)) :
        cal[i][j] = abs(home_idx[i][0]-chic_idx[j][0]) + abs((home_idx[i][1]-chic_idx[j][1]))
        hap[j] += cal[i][j]

if m == len(hap) :
    for i in range(len(home_idx)) :
        answer += min(cal[i])
else :
    
    for i in range(m) :
        a = min(hap)
        print(a)
        a_idx = hap.index(a)
        b.append(a_idx)
        hap[a_idx] = max(hap)
    print(b)
print(cal)


# for i in range(m) :
#     answer += min(cal[][], cal[])


print(answer)