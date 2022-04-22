n = int(input())
school = []
teacher = []
blank = []
temp = [[0]*n for _ in range(n)]
for i in range(n) :
    school.append(list(map(str, input().split())))
    for j in range(n) :
        if school[i][j] == 'T' :
            teacher.append([i,j])
        if school[i][j] == 'X' :
            blank.append([i,j])
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def search() :
    for t in teacher :
        for i in range(4) :
            nx = dx[i] + t[0]
            ny = dy[i] + t[1]
            while nx < n and nx >= 0 and ny < n and ny >= 0:
                if temp[nx][ny] == 'S' :
                    return False
                if temp[nx][ny] == 'O' :
                    break
    return True

def ob(cnt) :
    if cnt == 3 :
        for i in range(n) :
            for j in range(n) :
                temp[i][j] = school[i][j]


    else :
        for i in range(n) :
            for j in range(n) :
                if school[i][j] == 'X' :
                    school[i][j] = 'O'
                    ob(cnt+1)
                    school[i][j] = 'X'
