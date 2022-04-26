from collections import deque

def propagation(actvirus) :
    global maxv
    q = deque()
    temp = [[-1]*n for _ in range(n)]
    for pos in actvirus :
        temp[pos[0]][pos[1]] = 0
        q.append(pos)
    maxv = 0 # 종료 시점 걸리는 시간 구하려고 사용
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=0 and nx < n and ny >=0 and ny<n :
                if temp[nx][ny] == -1 and lab[nx][ny]!=1:
                    temp[nx][ny] = temp[x][y] + 1
                    if lab[nx][ny] == 0 :
                        maxv = max(maxv, temp[nx][ny])
                    q.append((nx,ny))

    for i in range(n) :
        for j in range(n) :
            if temp[i][j] == -1 and lab[i][j] !=1:
                maxv = 0
                return False
    return True


def comb(arr,n) :
    result = []
    if len(arr) < n :
        return arr
    if n==1 :
        for i in arr :
            result.append([i])
    if n > 1 :
        for i in range(len(arr)-n+1) :
            for j in comb(arr[i+1:], n-1) :
                result.append([arr[i]]+j)
    return result


if __name__ == "__main__" :
    a = 0
    n, m = map(int, input().split())
    lab = []
    wall = []
    temp = [[0]*n for i in range(n)]
    virus_pos = []
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    time = 1e9
    for i in range(n) :
        lab.append(list(map(int, input().split())))
        for j in range(n) :
            if lab[i][j] == 1 :
                wall.append([i,j])
            if lab[i][j] == 2 :
                virus_pos.append([i,j])

    for actvirus in comb(virus_pos,m) :
        mintime = propagation(actvirus)
        if mintime == False :
            continue
        else :
            time = min(time, maxv)

    if time == 1e9 :
        print(-1)
    else :
        print(time)