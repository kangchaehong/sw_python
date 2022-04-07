p = '(()())()'
def solution(p):
    dfs(p)
    answer = ''

    return answer

def dfs(p) :
    left = 0
    right = 0
    if len(p) == 0 :
        return
    if len(p) > 0 :
        for i in range(len(p)) :
            if p[i] == '(' :
                left += 1
            else :
                right += 1
        
            u = p[:i+1]
            v = p[i+2:]
            print(u)
            print(v)

solution(p)