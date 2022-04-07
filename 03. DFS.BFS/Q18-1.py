def balance_check(p) :
    count = 0
    for i in range(len(p)) :
        if p[i] == '(' :
            count += 1
        else :
            count -= 1

        if count == 0 :
            return i
    # return i

def right_check(p) :
    count = 0
    for i in p :
        if i == '(' :
            count += 1
        else :
            count -= 1
        # 쌍이 맞지 않는 경우
        if count < 0 :
            return False
    # 전체 쌍이 맞는 경우
    if count == 0 :
        return True
    else :
        return False

def solution(p):
    if len(p) == 0 :
        return ''

    index = balance_check(p)
    u = list(p[:index+1])
    v = list(p[index+1: ])
    ans = solution(v)
    # 올바른 문자열 아닌 경우
    if right_check(u) == False :
        u = u[1: -1]
        for j in range(len(u)) :
            if u[j] == '(' :
                u[j] = ')'
            else :
                u[j] = '('
        u = "".join(u)
        answer = '(' + ans + ')' + u
    # 올바른 문자열인 경우
    else :
        u = "".join(u)
        answer = u + ans
    return answer

p = '(()())()'
print(solution(p))

a = ')('
print(solution(a))

b = '()))((()'
print(solution(b))