def dfs(x,y,cnt,total):
    global maxv
    if cnt == 3 :
        maxv = max(total, maxv)
        return

    else :
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < n and nx >=0 and ny >=0 and ny<m and visited[nx][ny] == 0 :
                if cnt == 1:
                    visited[nx][ny] = 1
                    dfs(x,y,cnt+1, total+paper[nx][ny])
                    visited[nx][ny] = 0
                visited[nx][ny] = 1
                dfs(nx,ny,cnt+1, total+paper[nx][ny])
                visited[nx][ny] = 0

if __name__ == "__main__" :
    n,m = map(int,input().split())
    paper = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    total = 0
    maxv = 0

    for i in range(n) :
        for j in range(m) :
            visited[i][j] = 1
            dfs(i,j,0,paper[i][j])
            visited[i][j]=0
    print(maxv)