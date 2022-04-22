n = 5
build_frame =[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

def check(result) :
    for x,y,stuff in result :
        if stuff == 0:
            if y == 0 or ([x,y-1,0] in result) or ([x,y,1] in result) or ([x-1,y,1] in result) :
                continue
            else :
                return False
        elif stuff == 1 :
            if ([x,y-1,0] in result) or ([x+1, y-1,0] in result) or (([x-1,y,1] in result) and ([x+1,y,1] in result)) :
                continue
            else :
                return False
    return True


def solution(n, build_frame):
    result = []
    for x,y,stuff,install in build_frame :
        if install == 1 :
            result.append([x,y,stuff])
            answer = check(result)
            if answer == False :
                result.remove([x,y,stuff])
        elif install == 0 :
            result.remove([x,y,stuff])
            answer = check(result)
            if answer == False :
                result.append([x,y,stuff])
        # print(result)
    result.sort(key=lambda x : (x[0],x[1],x[2]))
    return result

print(solution(n, build_frame))


