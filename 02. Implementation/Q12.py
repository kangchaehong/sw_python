def check(answer):
    for x,y,stuff in answer :
        # if x < 0 or x > n or y < 0 or y > n:
        #     return False

        if stuff == 0 :
            if y == 0 or [x, y, 1] in answer or [x, y-1, 0] in answer or [x-1, y, 1] in answer :
                continue
            return False

        elif stuff == 1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or [x,y-1,0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame :
        x, y, stuff, operate = frame
        if operate == 0 : # 삭제하는 경우
            answer.remove([x, y, stuff]) # 일단 삭제
            if not check(answer) : # 가능한지 체크
                answer.append([x,y,stuff]) # 안되면 다시 추가
        if operate == 1 : # 설치하는 경우
            answer.append([x, y, stuff]) # 일단 추가
            if not check(answer) : # 가능한지 체크
                answer.remove([x, y, stuff]) # 안되면 다시 지우기

    return sorted(answer)

n = 5
a = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n,a))