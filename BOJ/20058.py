from collections import deque
import copy

def rotate(div) :
    global rice
    L = 2**div
    for a in range(0,2**n,L) :
        for b in range(0,2**n,L) :
            for i in range(L) :
                for j in range(L) :
                    rice[j+a][L-i-1+b] = ice[i+a][j+b]

def hotice() :
    water = [] # 녹여야하는 칸
    for x in range(length) :
        for y in range(length) :
            ice_cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= length or nx < 0 or ny < 0 or ny >= length :
                    ice_cnt += 1

                if nx < length and nx >= 0 and ny>=0 and ny < length :
                    if rice[nx][ny] == 0 :
                        ice_cnt += 1
            if ice_cnt > 1 and rice[x][y] != 0:
                water.append([x,y])
    for a,b in water :
        rice[a][b] -= 1


def countice(i,j) :
    global visited, area
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    area = 0
    while q :
        x,y = q.popleft()
        area += 1
        for k in range(4) :
            nx = x + dx[k]
            ny = y + dy[k]
            if nx >=0 and nx < length and ny>=0 and ny < length :
                if visited[nx][ny] == 0 and rice[nx][ny] !=0 :
                    visited[nx][ny] = 1
                    q.append((nx,ny))
    return area

if __name__ == "__main__" :
    n, q = map(int, input().split())
    ice = [list(map(int, input().split())) for _ in range(2 ** n)]
    l = list(map(int, input().split()))

    rice = [[0] * (2 ** n) for _ in range(2 ** n)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    length = 2**n
    total = -1e9
    totalsum = 0
    area = 0

    for _l in l :
        rotate(_l)
        hotice()
        ice = copy.deepcopy(rice)

    visited = [[0] * (2 ** n) for _ in range(2 ** n)]

    for i in range(length) :
        totalsum += sum(rice[i])
        for j in range(length) :
            if rice[i][j] != 0 and visited[i][j] == 0:
                area = countice(i,j)
            total = max(total, area)
    print(totalsum)
    print(total)
