import copy
from collections import deque

r,c,t = map(int, input().split())
a = []
dust = [] # 미세먼지 위치
clean = [] # 공기 청정기 위치

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(r) :
    a.append(list(map(int, input().split())))
    for j in range(c) :
        if a[i][j] == -1 :
            clean.append((i,j))

# 미세먼지 전파
def propa(a) :
    new_dust = [[0]*c for _ in range(r)]
    for x in range(r) :
        for y in range(c) :
            if a[x][y] != 0 and a[x][y] != -1:
                dcnt = 0
                for i in range(4) :
                    nx = x+dx[i]
                    ny = y+dy[i]
                    if nx<r and nx>=0 and ny<c and ny>=0 and (nx,ny) not in clean :
                        new_dust[nx][ny] += int(a[x][y]/5)
                        dcnt += 1
                new_dust[x][y] += int((a[x][y]-(int(a[x][y]/5)*dcnt)))
    return new_dust

# 공기청정기 작동
def fair(new_dust) :
    cnt = 0
    # print(new_dust)
    for x,y in clean :
        endx, endy = x,y
        if cnt == 0 :
            y = y+1
            up_step = [[0,1],[-1,0],[0,-1],[1,0]]
            stepcnt = 0
            prev = 0
            while True :
                nx, ny = x+up_step[stepcnt][0], y+up_step[stepcnt][1]
                if x == endx and y == endy :
                    break
                if nx >= r or nx < 0 or ny >= c or ny < 0 :
                    stepcnt += 1
                    continue
                new_dust[x][y], prev = prev, new_dust[x][y]
                x,y = nx, ny
            cnt +=1

        elif cnt == 1:
            down_step = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            # print(a, endx,endy)
            stepcnt = 0
            y = 1
            prev = 0
            while True:
                nx, ny = x + down_step[stepcnt][0], y + down_step[stepcnt][1]
                if x == endx and y == endy:
                    break
                if nx >= r or nx < 0 or ny >= c or ny < 0:
                    stepcnt += 1
                    continue
                new_dust[x][y], prev = prev, new_dust[x][y]
                x, y = nx, ny
    return new_dust

for _ in range(t) :
    dustval = 0
    new = propa(a)
    a = fair(new)

totalval = 0
for i in range(r) :
    for j in range(c) :
        totalval += a[i][j]
print(totalval)

