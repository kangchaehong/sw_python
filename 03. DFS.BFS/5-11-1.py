from collections import deque
n, m = map(int, input().split())
miro = []
for i in range(n) :
    miro.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y) :
    q = deque()
    q.append((x, y))
    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= n or nx < 0 or ny >= m or ny < 0 :
                continue
            if miro[nx][ny] == 1 :
                miro[nx][ny] = miro[x][y] + 1
                q.append((nx, ny))
            else :
                continue
    print(miro)

    return miro[n-1][m-1]
print(bfs(0,0))