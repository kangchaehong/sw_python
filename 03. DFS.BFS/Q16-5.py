n, m = map(int, input().split())
lab = []
for _ in range(n) :
    lab.append(list(map(int, input().split())))
dx = [0,0,-1,1]
dy = [-1,1,0,0]
temp = [[0]*m for _ in range(n)]
total = -1

# 벽 세우는 코드
def wall(cnt) :
    global total

    if cnt == 3 :
        for i in range(n):
            for j in range(m):
                temp[i][j] = lab[i][j]
        # print(lab)
        for i in range(n) :
            for j in range(m) :
                if temp[i][j] == 2 :
                    virus(i,j)

        result = getscore()
        total = max(result,total)
        return

    for i in range(n) :
        for j in range(m) :
            if lab[i][j] == 0:
                lab[i][j] = 1
                cnt += 1
                wall(cnt)
                lab[i][j] = 0
                cnt -= 1
    # return total

# 바이러스 전파 코드
def virus(x,y) :
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<m :
            if temp[nx][ny]==0 :
                temp[nx][ny] = 2
                virus(nx,ny)
    # print(temp)

# 남은 공간 여부 확인
def getscore() :
    result=0
    for i in range(n) :
        for j in range(m) :
            if temp[i][j] == 0 :
                result+=1
    return result
wall(0)
print(total)