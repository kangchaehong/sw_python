def check(result) :
    for x,y,stuff in result :
        if stuff == 0 :
            if y == 0 or [x,y,1] in result or [x,y-1,0] in result or [x-1,y,1] in result :
                continue
            return False
        if stuff == 1 :
            if [x,y-1,0] in result or [x+1, y-1, 0] in result or ([x-1,y,1] in result and [x+1,y,1] in result) :
                continue
            return False
    return True

def solution(n, build_frame):
    result = []
    for i in build_frame :
        x, y, stuff, operate = i
        if operate == 0 :
            result.remove([x,y,stuff])
            if not check(result) :
                result.append([x,y,stuff])
        elif operate == 1 :
            result.append([x,y,stuff])
            if not check(result) :
                result.remove([x,y,stuff])
    return sorted(result)

n = 5
build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
print(solution(n,build_frame))