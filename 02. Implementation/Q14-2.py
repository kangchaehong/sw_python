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
    return result

def solution(n, weak, dist) :
    length = len(weak)
    for i in range(length) :
        weak.append(weak[i]+n)

    answer = len(dist) + 1

    for start in range(length) :
        for friends in perm(dist, len(dist)) :
            count = 1
            position = weak[start] + friends[count-1]


            for index in range(start, start+length) :
                if position < weak[index] :
                    count += 1
                    if count > len(dist) :
                        break
                    position = weak[index] + friends[count-1]
            answer = min(answer,count)
    if answer > len(dist) :
        return -1
    return answer

