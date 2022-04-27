import copy
from collections import deque

def friendremove(x,y) :
    global removearr
    q = deque()
    q.append((x,y))
    while q :
        x,y = q.popleft()
        for k in range(4) :
            nx = x + dx[k]
            ny = y + dy[k]
            if ny < 0 :
                ny = m-1
            elif ny > m-1 :
                ny = 0
            if nx < n and nx >= 0 and ny < m and ny >= 0 and visited[nx][ny] == 0 :
                if circle[nx][ny] == circle[x][y]:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    visited[x][y] = 1
                    # removearr.add((nx,ny))
                    # removearr.add((x,y))
    # return removearr

if __name__ == "__main__" :
    n,m,t = map(int, input().split())
    circle = [list(map(int, input().split())) for _ in range(n)]
    # 0:x / 1:d / 2:k
    direction = [list(map(int, input().split())) for _ in range(t)]
    dir = [1,-1]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for _ in range(t) :
        temp = copy.deepcopy(circle)
        x,d,k = direction.pop(0)
        # 회전
        for i in range(x-1, n, x) :
            for j in range(m) :
                nj = j + (dir[d]*k)
                if nj < 0 or nj >= m :
                    nj = nj % m
                circle[i][nj] = temp[i][j]

        # 원판에 수가 있는지 확인
        temp_num = 0
        for num in circle:
            temp_num += sum(num)
        # 원판에 수가 없으면 break
        if temp_num == 0:
            break

        # 인접 값 지우기
        visited = [[0] * m for _ in range(n)]
        newmove = []
        suma = 0
        div = 0
        cnt0 = 0

        for i in range(n) :
            for j in range(m) :
                if visited[i][j] == 0 and circle[i][j] != 0:
                    friendremove(i,j)
                    # newremove = friendremove(i,j)
                #     if len(newremove) > 1 :
                #         for remv in newremove :
                #             # print(remv)
                #             circle[remv[0]][remv[1]] = 0
                #             cnt0 += 1
                # sum += circle[i][j]
                # if circle[i][j] >= 1 :
                #     div += 1

        # 방문했으면 인접한거!
        for ii in range(n) :
            for jj in range(m) :
                if visited[ii][jj] == 1 :
                    circle[ii][jj]=0
                    cnt0 = 1

        if cnt0 == 0 :
            for ia in range(n) :
                for ja in range(m) :
                    if circle[ia][ja] != 0 :
                        suma += circle[ia][ja]
                        div += 1
            avg = suma / div
            for ib in range(n) :
                for jb in range(m) :
                    if circle[ib][jb] != 0 :
                        if circle[ib][jb] > avg :
                            circle[ib][jb] -= 1
                        elif circle[ib][jb] < avg :
                            circle[ib][jb] += 1
        print(circle)
    ttt = 0
    for idx in range(n) :
        ttt += sum(circle[idx])
    print(ttt)