from collections import deque

def bfs(x,y) :
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    changexy = [(x,y)]
    sum = union[x][y]
    while q :
        x,y = q.popleft()
        for k in range(4) :
            nx = x + dx[k]
            ny = y + dy[k]
            if nx>=0 and nx<n and ny>=0 and ny<n and visited[nx][ny] == False :
                if l<= abs(union[nx][ny]-union[x][y]) <=r :
                    changexy.append((nx,ny))
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    sum += union[nx][ny]
    for x,y in changexy :
        union[x][y] = int(sum/len(changexy))

    length = len(changexy)
    return length

if __name__ == "__main__" :
    n,l,r = map(int, input().split())
    union = [list(map(int, input().split())) for _ in range(n)]
    # print(union)
    change = 0
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    while True :
        visited = [[False]*n for _ in range(n)]
        flag = False
        for i in range(n) :
            for j in range(n) :
                if not visited[i][j] :
                    if bfs(i,j) > 1 :
                        flag = True
        if not flag :
            break
        change += 1
    print(change)