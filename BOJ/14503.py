from collections import deque
def dfs(r,c,d) :
    global move
    q = deque()
    q.append([r,c,d])
    while q :
        cnt = 0
        x,y,d = q.popleft()
        for i in range(4) :
            d = (d+3)%4
            nx = x + dx[d]
            ny = y + dy[d]

            if nx >=0 and nx < n and ny >=0 and ny < m :
                if clean[nx][ny]==0:
                    q.append((nx, ny,d))
                    clean[nx][ny] = 2
                    move += 1
                    break
                else :
                    cnt += 1
        if cnt == 4 :
            nx = x + dx[(d + 2) % 4]
            ny = y + dy[(d + 2) % 4]
            if clean[nx][ny] != 1:
                q.append((nx, ny, d))
                # move += 1
                clean[nx][ny] = 2
            else :
                return move


if __name__ == "__main__" :
    n, m = map(int, input().split())
    r,c,d = map(int, input().split())
    clean = [list(map(int, input().split())) for _ in range(n)]
    move = 1
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    clean[r][c] = 2
    dfs(r,c,d)
    print(move)