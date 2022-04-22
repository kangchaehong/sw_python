n = int(input())
school, student, teacher = [],[],[]
temp =[[0]*n for _ in range(n)]
for i in range(n) :
    school.append(list(map(str, input().split())))
    for j in range(n) :
        if school[i][j] == 'T' :
            teacher.append([i,j])

dx = [0,0,-1,1]
dy = [1,-1,0,0]
find = 'NO'

def dfs() :
    # print(temp)
    for t in teacher:
        for i in range(4) :
            x,y = t
            while x >= 0 and x < n and y >= 0 and y < n :
                if temp[x][y] == 'O':
                    break
                elif temp[x][y] == 'S' :
                    return False
                x += dx[i]
                y += dy[i]
    return True

def obsatcle(cnt) :
    global find
    if cnt > 3 :
        return
    if cnt == 3 :
        for i in range(n):
            for j in range(n) :
                temp[i][j] = school[i][j]

        if dfs() is True :
            find = 'YES'
            return
        else :
            find ='NO'

    for i in range(n) :
        for j in range(n) :
            if school[i][j] == 'X' :
                school[i][j] = 'O'
                # print(school)
                cnt+=1
                obsatcle(cnt)
                if find == 'YES' :
                    return
                school[i][j] = 'X'
                cnt-=1
obsatcle(0)
print(find)