# from itertools import permutations
def perm(arr, n) :
    result = []
    if len(arr) < n :
        return arr
    if n == 1 :
        for i in arr :
            result.append([i])
    elif n > 1 :
        for i in range(len(arr)) :
            ans = [i for i in arr]
            ans.remove(arr[i])
            for j in perm(ans, n-1) :
                result.append([arr[i]]+j)
    # result.sort(reverse=True)
    result.sort(key=lambda x : -x[0])
    return result

def solution(n, weak,dist) :
    total = len(dist)+1
    length = len(weak)
    # new_weak  = [0]*(len(weak))
    for i in range(len(weak)) :
        weak.append(weak[i]+n)
    for friend in perm(dist, len(dist)):
        for i in range(length):
    # for friend in list(permutations(dist, len(dist))):
            cnt = 1
            idx = 0
            position = weak[i] + friend[idx]
            for j in range(i, i+length) :
                if position < weak[j] :
                    cnt += 1
                    idx += 1
                    if cnt > len(dist) :
                        break
                    position = weak[j] + friend[idx]
            total = min(total, cnt)
    if total > len(dist) :
        return -1
    return total

print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]))