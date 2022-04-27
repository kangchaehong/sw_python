from collections import deque

def goto(x,y,dist, cartocus, cartodest) :
    visited = [[0]*n for _ in range(n)]
    tempcus = []
    q = deque()
    q.append((x,y,dist))
    while q :
        x,y,d = q.popleft()
        visited[x][y] = 1
        # print(ttcus)
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >=0 and nx < n and ny >= 0 and ny < n and visited[nx][ny] == 0 and drive[nx][ny] != 1:
                if cartocus == 1 :
                    q.append((nx,ny,d+1))
                    visited[nx][ny] = 1

                    if [nx,ny] in ttcus :
                        tempcus.append([nx,ny,d])
                    # if [x,y] in ttcus :
                    #     tempcus.append([x,y,0])

                if cartodest == 1 :
                    q.append((nx,ny,d+1))
                    visited[nx][ny] = 1
                    if [nx,ny] in tempdest :
                        return nx, ny, d
    # print(tempcus)
    if len(tempcus) > 0 :
        tempcus.sort(key=lambda x: (x[2], x[0], x[1]))
        tempcus = tempcus[0]
        return tempcus[0], tempcus[1], tempcus[2]
        # nnx, nny, dist = tempcus[0], tempcus[1], tempcus[2]
    return False

n,m,gas = map(int, input().split())
drive = [list(map(int, input().split())) for _ in range(n)]
car = list(map(int,input().split()))
cus = []
ttcus = []
dest = []

for i in range(m) :
    cx,cy,drx,dry = map(int, input().split())
    cus.append([cx-1,cy-1])
    ttcus.append([cx-1, cy-1])
    dest.append([drx-1,dry-1])

dx = [-1,1,0,0]
dy = [0,0,-1,1]

carx, cary = car[0]-1, car[1]-1
breakp = False
for _ in range(m) :
    tempdest = []

    if goto(carx, cary, 1, 1, 0):
        if [carx,cary] in ttcus :
            nnx,nny,dist = carx,cary,0
        else :
            nnx, nny, dist = goto(carx, cary, 1, 1, 0)
    else :
        breakp = True
        break

    for i in range(len(cus)) :
        if cus[i][0] == nnx and cus[i][1] == nny :
            tempdest.append([dest[i][0], dest[i][1]])
    ttcus.remove([nnx,nny])
    gas -= dist
    if gas < 0 :
        breakp = True
        break

    if goto(nnx,nny,1,0,1) :
       carx, cary, dd = goto(nnx,nny,1,0,1)

    else :
        breakp = True
        break

    gas -= dd
    if gas < 0 :
        breakp = True
        break
    gas += (dd)*2

if breakp :
    print(-1)
else :
    print(gas)
