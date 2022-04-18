# 입력부
n = int(input())
school,teacher,blank,temp = [],[],[],[]

for i in range(n) :
    school.append(list(input().split()))
    temp.append(school[i])
    for j in range(n) :
        if school[i][j] == 'X' :
            blank.append([i,j])
        elif school[i][j] == 'T' :
            teacher.append([i,j])

# 변수
dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 장애물 조합 찾기
def comb(arr, n) :
    result = []
    if len(arr) < n :
        return arr
    if n == 1 :
        for i in arr :
            result.append([i])
    elif n > 1 :
        for i in range(len(arr)-n+1) :
            for j in comb(arr[i+1:], n-1):
                result.append([arr[i]]+j)
    return result

# 탐색부
def dfs(tx,ty,dir) :
    if dir == 0 :
        while ty < n :
            # print(dir,tx, ty)
            if temp[tx][ty] == 'O' :
                return False
            if temp[tx][ty] == 'S' :
                return True
            ty += 1
    elif dir == 1 :
        while ty >= 0 :
            # print(dir,tx, ty)
            if temp[tx][ty] == 'O' :
                return False
            if temp[tx][ty] == 'S' :
                return True
            ty -= 1
    elif dir == 2 :
        while tx >= 0 :
            # print(dir,tx, ty)
            if temp[tx][ty] == 'O' :
                return False
            if temp[tx][ty] == 'S' :
                return True
            tx -= 1
    elif dir == 3 :
        while tx < n :
            # print(dir,tx,ty)
            if temp[tx][ty] == 'O' :
                return False
            if temp[tx][ty] == 'S' :
                return True
            tx += 1
    return False

def process() :
    for tx, ty in teacher:
        for i in range(4):
            if dfs(tx,ty,i) :
                return True
    return False

# 수행부 : 찾으면 no 못찾으면 yes
def simulate() :
    find = False
    ob = comb(blank,3)
    for obs in ob :
        for x,y in obs :
            temp[x][y] = 'O'
            # print(temp)
            if not process():
                find = True
                break
        for x,y in obs :
            temp[x][y] = 'X'
    if find:
        print('YES')
    else :
        print('NO')

simulate()