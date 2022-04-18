n,m = map(int, input().split())
chicken = []
home = []
store = []
for i in range(n) :
    chicken.append(list(map(int, input().split())))
    for j in range(n) :
        if chicken[i][j] == 1 :
            home.append((i,j))
        if chicken[i][j] == 2 :
            store.append((i,j))

def comb(arr, n) :
    result = []
    if len(arr) < n :
        return arr
    if n == 1 :
        for i in arr :
            result.append([i])
    elif n > 1 :
        for i in range(len(arr)-n+1) :
            for j in comb(arr[i+1:], n-1) :
                result.append([arr[i]]+j)
    return result

def distance() :
    chicomb = comb(store, m)
    chic_dist = []
    sum = 0
    min_v = 1e9
    for i in chicomb :
        for j in home :
            for k in range(m) :
                min_v = min(min_v, abs(i[k][0]-j[0])+abs(i[k][1]-j[1]))
            sum += min_v
            min_v = 1e9
        chic_dist.append(sum)
        sum = 0
    return min(chic_dist)
print(distance())


