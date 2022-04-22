n, m = map(int, input().split())
city, home, chicken = [],[],[]
for i in range(n) :
    city.append(list(map(int, input().split())))
    for j in range(n) :
        if city[i][j] == 1 :
            home.append([i,j])
        if city[i][j] == 2 :
            chicken.append([i,j])

def comb(arr,m) :
    result = []
    if len(arr) < m :
        return arr
    if m == 1 :
        for i in arr :
            result.append([i])
    if m > 1 :
        for i in range(len(arr)-m+1) :
            for j in comb(arr[i+1:], m-1) :
                result.append([arr[i]]+j)
    return result

def solution() :
    total_minv = 0 # 치킨 1 조합 당 치킨 거리 총합
    result = 1e9 # 최종 최소값
    minv = 1e9  # 치킨 1개 당 치킨 거리
    chicken_list = comb(chicken, m)
    for chicken_step in chicken_list :
        for hx, hy in home:
            for cx,cy in chicken_step :
                chicken_dist = abs(cx-hx) + abs(cy-hy)
                minv = min(chicken_dist, minv)
            total_minv += minv
            minv = 1e9  # 치킨 1개 당 치킨 거리
        result = min(total_minv,result)
        total_minv = 0

    print(result)

solution()