def solution(s):
    length = int(len(s) / 2)
    answer = len(s)

    for step in range(1, length+1) :
        compressed = ""
        prev = s[0:step]
        cnt = 1
        for i in range(step, len(s), step) :
            if prev == s[i:i + step] :
                cnt += 1
                prev = s[i:i + step]
            else :
                compressed += str(cnt) + prev if cnt >=2 else prev
                prev = s[i:i + step]
                cnt = 1
        compressed += str(cnt) + prev if cnt >=2 else prev
        answer = min(answer, len(compressed))

    return answer

sb ="abcabcddde"
print(solution(sb))


