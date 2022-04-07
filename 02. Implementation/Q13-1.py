from itertools import combinations

# combination 외우기!!+

def comb(arr, n) :
    result = []
    if n > len(arr) :
        return result
    if n == 1 :
        for i in arr :
            result.append([i])
    elif n > 1 :
        for i in range(len(arr)-n+1) :
            for j in comb(arr[i+1 :], n-1):
                result.append([arr[i]]+j)
    return result

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n) :
    data = list(map(int, input().split()))
    for c in range(n) :
        if data[c] == 1 :
            house.append((r,c))
        elif data[c] == 2 :
            chicken.append((r,c))

# candidates = list(combinations(chicken, m))
candidates = comb(chicken,m)

# 집 하나당 선택된 치킨집과의 거리들 다 구하고 최솟값만 return
def get_sum(candidates) :
    result = 0
    for hx, hy in house :
        temp = 1e9
        for cx, cy in candidates :
            temp = min(temp, abs(hx-cx)+abs(hy-cy))
        result += temp
    return result

result = 1e9
# 리턴된 조합들 중 가장 최소의 거리 가지는 조삽
for candidate in candidates :
    result = min(result, get_sum(candidate))

print(result)
