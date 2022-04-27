from collections import deque

def moveshark() :
    global moving
    moving = []
    visited = [[0]*n for _ in range(n)]
    q = deque()
    q.append([shark[0][0],shark[0][1],0])
    sx, sy, sm = shark[0][0], shark[0][1], shark[0][2]
    sea[sx][sy] = 0

    while q :
        x, y, dist = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 초과, 상어==물고기면 이동 가능
            if nx >= 0 and nx < n and ny >= 0 and ny < n and sea[nx][ny] <= sm and visited[nx][ny] == 0:
                # 상어보다 물고기 크기 작은 경우 먹을 수 있음
                if 0 < sea[nx][ny] < sm:
                   moving.append([nx,ny,sea[nx][ny],dist+1])
                   visited[nx][ny] = 1
                q.append([nx,ny, dist+1])
                visited[nx][ny] = 1
    moving.sort(key=lambda x :(x[3],x[0],x[1]))


def eating() :
    global eatcnt, move
    if len(moving) == 0 :
        return False
    sx, sy, sm = shark.pop(0)
    mx, my, mm, md = moving.pop(0)
    eatcnt += 1
    if eatcnt == sm :
        sm+=1
        eatcnt = 0
    shark.append([mx,my,sm])
    move += md
    return True


if __name__ == "__main__" :
    n = int(input())
    sea = []
    shark = []
    fish = []
    move = 0 # 이동횟수
    eatcnt = 0
    for i in range(n) :
        sea.append(list(map(int, input().split())))
        for j in range(n) :
            if sea[i][j] == 9 :
                shark.append([i,j,2])

    next_sea = [[0]*n for _ in range(n)]

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while True :
        moveshark()
        if eating() == False :
            break
    print(move)
