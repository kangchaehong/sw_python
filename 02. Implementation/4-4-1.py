n, m = map(int, input().split())
x,y,d = map(int, input().split())
game = []
visited = []
for i in range(n) :
    game.append(list(map(int, input().split())))
    visited.append(game[i])

# 북동남서
dx =[-1,0,1,0]
dy = [0,1,0,-1]

count = 1 # 방문 칸 횟수
rotate = 0 # 회전 횟수
visited[x][y] = 1 # 초기 방문 값 설정

while True :
    d = (d-1) % 4 # 회전 수행
    # 이동
    nx = x + dx[d]
    ny = y + dy[d]

    if game[nx][ny] == 0 and visited[nx][ny] == 0:
        x = nx
        y = ny
        visited[x][y] = 1
        rotate = 0
        count += 1
    else :
        rotate += 1

    if rotate == 4 :
        d = (d+2) % 4 # 뒤로 방향 바꾸기
        nx = x + dx[d]
        ny = y + dy[d]

        if game[nx][ny] == 1 :
            break
        else :
            x = nx
            y = ny
            rotate = 0
            
print(count)
