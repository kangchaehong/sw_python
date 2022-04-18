def balance(p) :
    cnt = 0
    index = 0
    for i in range(len(p)) :
        if '(' == p[i] :
            cnt += 1
        else :
            cnt -= 1
        if cnt == 0 :
            index = i
            return index
    return index

def right(p) :
    count = 0
    for i in range(len(p)) :
        if p[i] == '(' :
            count += 1
        else :
            count -= 1
        if count < 0 :
            return False
    return True

def solution(p):
    if len(p) == 0 :
        return p

    index = balance(p)
    u = p[ :index+1]
    v = p[index+1:]

    if right(u) == True : # 올바른 문자열이라면
        str = solution(v)
        str = u + str
    elif right(u) == False : # 올바른 문자열이 아니라면
        str = '(' + solution(v) + ')'
        u = u[1:-1]
        for i in range(len(u)) :
            if u[i] == '(' :
                u = u[:i] + ')' + u[i+1:]
            else :
                u = u[:i] + '(' + u[i + 1:]

        str = str + u
    return str
p = ")("
print(solution(p))

