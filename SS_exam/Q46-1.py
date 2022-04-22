from collections import deque
# 입력부
n = int(input())
sea=[]
for i in range(n) :
    sea.append(list(map(int, input().split())))
    for j in range(n) :
        if sea[i][j] == 9 :
            # 상어 있던 곳 0 처리 필수
            sea[i][j] = 0
            sx = i
            sy = j

# 변수부
size = 2
dx = [0,0,-1,1]
dy = [1,-1,0,0]
count = 0
move = 0
eat = 0

# 실행부
while True :
    visited = [[False]*n for _ in range(n)]
    fish_list=[]
    # 할떄마다 새로 queue 선언!
    q = deque()
    q.append((sx, sy, 0))
    # flag 다시 설정해야하므로!! 여기에 변수 선언!
    flag = 1e9
    while q :
        x, y, count = q.popleft()
        if count > flag:
            break
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n :
                if sea[nx][ny] > size or visited[nx][ny] :
                    continue
                if sea[nx][ny] < size and sea[nx][ny] != 0 :
                    fish_list.append((nx,ny,count+1))
                    # print(fish_list)
                    flag = count
                q.append((nx,ny,count+1))
                visited[nx][ny] = True
# 메인 실행부
    if len(fish_list) > 0 :
        fish_list.sort()
        # print(fish_list)
        sx, sy = fish_list[0][0], fish_list[0][1]
        move += fish_list[0][2]
        eat += 1
        # 먹이 먹은 곳 0 처리 해줘야함!!
        sea[sx][sy] = 0
        if size == eat :
            size += 1
            eat = 0
        # q.append((sx,sy,count+1))
        # print('11',q)
    else :
        break
print(move)