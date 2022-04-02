def solution(s):
    length = len(s)
    max = length // 2
    cnt = 1
    answerl = ''
    for i in range(max,0,-1):
        if s[:i] == s[i:2*i] :
            cut = i
            break
        else :
            cut = length

    if cut == length :
        answer = length
        return answer

    if length % cut == 0 :
        circle = (length // cut)-1
    else :
        circle = (length // cut)

    for j in range(1,circle+1):
        r = j*cut
        if s[r-cut:r] == s[r:r+cut] :
            cnt += 1
            word = s[r-cut:r]
        else :
            if cnt == 1 :
                answerl = answerl + s[r-cut:r]
                continue
            answerl = answerl + str(cnt) + word
            cnt = 1
        if j == circle :
            answerl = answerl + str(cnt) + word

    if length % cut != 0:
        answerl = answerl + s[-(length % cut):]

    answer = len(answerl)
    return answer


sb ="abcabcdede"
print(solution(sb))


