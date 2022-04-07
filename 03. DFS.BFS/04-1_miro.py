from collections import deque

n, m = map(int, input().split())
miro = []
for i in range(n) :
    miro.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y) :
    queue = deque()
    queue.append((x,y))

    while queue :
        a, b = queue.popleft()
        for i in range(4) :
            nx = a+dx[i]
            ny = b+dy[i]
            if nx < 0 or nx >= n or ny<0 or ny >= m :
                continue
            if miro[nx][ny] == 0 :
                continue
            if miro[nx][ny] == 1 :
                miro[nx][ny] = miro[a][b] + 1
                queue.append((nx,ny))

    print(miro)
    return miro[n-1][m-1]

print(bfs(0,0))