def solution(s):
    l = len(s) // 2
    answer = len(s)
    for i in range(1,l+1) :
        step = i
        cnt = 1
        result = ''
        # print('i>>',i)
        for j in range(0, len(s), step) :
            prev = s[j:step + j]
            # print('>>>',s[j:step+j], s[j+step:(2*step)+j] )
            if s[j:step+j] == s[j+step:(2*step)+j] :
                cnt+=1
                # prev = s[j:step+j]
            else :
                if cnt > 1 :
                    result = result + str(cnt) + prev
                    cnt = 1
                    # prev =s[j+step:(2*step)+j]
                else :
                    result = result + prev
                    # prev = s[j+step:(2*step)+j]
        answer = min(answer, len(result))
        #     print(result)
        # print(len(result))
        # minlen.append(len(result))
    # return min(minlen)
    return answer
print(solution("xababcdcdababcdcd"))