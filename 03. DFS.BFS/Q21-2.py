from collections import deque
# 입력부
n,l,r = map(int, input().split())
union = []
for _ in range(n) :
    union.append(list(map(int, input().split())))
visited = [[False]*n for _ in range(n)]
count = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 수행부
def simulate() :
    for i in range(n):
        for j in range(n) :
            if visited[i][j] == False :
                bfs(i,j,visited)

            print('v',visited)
            print('c',count)
            print('u',union)


def bfs(x,y,visited) :
    q = deque()
    q.append((x,y))
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < n and nx >= 0 and ny < n and ny >= 0 and not (visited[nx][ny]) :
                if l <= abs(union[x][y]-union[nx][ny]) <= r :
                    visited[x][y] = True
                    print(visited)
                    visited[nx][ny] = True
                    q.append([nx,ny])
    sum()

def sum() :
    global count, visited
    avg = 0
    c = 0
    print('visit', visited)
    for i in range(n) :
        for j in range(n) :
            if visited[i][j] == True :
                avg += union[i][j]
                c += 1

    for i in range(n) :
        for j in range(n) :
            if visited[i][j] == True :
                union[i][j] = int(avg/c)

    visited = [[False] * n for _ in range(n)]
    count += 1
    print('c',count)
    return count

simulate()
print(count)