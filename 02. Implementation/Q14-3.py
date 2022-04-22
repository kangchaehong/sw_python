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

    result.sort(key=lambda x : -x[0])
    return result

def solution(n, weak,dist) :
    length = len(weak)
    for i in range(length) :
        weak.append(weak[i]+n)
    answer = len(dist) + 1
    for i in range(length) :
        for friend in perm(dist, len(dist)):
            count = 1
            position = weak[i] + friend[count-1]
            for index in range(i,i+length) :
                if position < weak[index] :
                    count += 1
                    if count > len(dist) :
                        break
                    position = weak[index] + friend[count-1]
            answer = min(answer, count)
    if answer > len(dist) :
        return -1
    return answer


n = 12
weak =[1, 5, 6, 10]
dist = [1,2,3,4]
print(solution(n, weak,dist))
