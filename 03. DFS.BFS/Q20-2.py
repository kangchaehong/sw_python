n = int(input())
school = []
teacher = []
result = 'NO'

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n) :
    school.append(list(input().split()))
    for j in range(n) :
        if school[i][j] == 'T' :
            teacher.append((i,j))

def check_t() :
    global teacher, school
    for t in teacher :
        for i in range(4) :
            x, y = t
            while x < n and x >= 0 and y < n and y >= 0 :
                # print(school)
                # if temp[nx][ny] == 'X' :
                #     temp[nx][ny] = 'T'
                if school[x][y] == 'S' :
                    return False
                elif school[x][y] == 'O' :
                    break
                x += dx[i]
                y += dy[i]
    return True

def dfs(count):
    global result, teacher, school
    if count > 3 :
        return
    if count == 3 :
        if check_t() is True :
            result = "YES"
            return
        else :
            result = 'NO'

    for i in range(n) :
        for j in range(n) :
            if school[i][j] == 'X' :
                school[i][j] = 'O'
                dfs(count+1)
                if result == 'YES' :
                    return
                school[i][j] = 'X'
                # print(school[i][j])
dfs(0)
print(result)

