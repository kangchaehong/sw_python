def solution(s):
    l = int(len(s) / 2)
    cnt = 1
    minv = len(s)
    while True :
        result = ''
        for i in range(l,len(s)+1,l):
            if s[i-l : i] == s[i:i+l] :
               cnt += 1
               rstr = s[i-l:i]
            else :
                if cnt != 1 :
                    result = result + str(cnt)+ rstr
                    cnt = 1
                else :
                    result = result + s[i-l:i]
        if len(s) % l != 0 :
            result = result + s[-(len(s) % l):]
        minv = min(len(result), minv)
        l -= 1
        if l == 0 :
            break
    return minv

print(solution("xababcdcdababcdcd"))
