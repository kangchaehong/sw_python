# 입력부
n = int(input())
apple_num = int(input())
apples = []
change = []
for _ in range(apple_num) :
    apples.append(list(map(int, input().split())))
l = int(input())
for _ in range(l) :
    change.append(list(map(str, input().split())))

garden = [[0]*(n+2) for _ in range(n+2)]
for x,y in apples :
    garden[x][y] = 1

def soultion() :
    cnt = 0  # 시간
    change_cnt = 0  # 초기 방향 좌표
    snake = [(1, 1)]  # 뱀 좌표 꼬리->머리 순
    dir = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while True :
        x = snake[-1][0]
        y = snake[-1][1]
        # print(cnt)
        # print(x,y)
        # print(snake)
        # print('-----')
        if len(change) >= change_cnt+1 :
            if change[change_cnt][0] == str(cnt) :
                if change[change_cnt][1] == 'D' :
                    dir=(dir+1)%4
                else :
                    dir=(dir-1)%4
                change_cnt += 1

        nx = x + dx[dir]
        ny = y + dy[dir]

        if nx < 1 or nx > n or ny < 1 or ny > n or (nx, ny) in snake:
            return cnt+1

        if garden[nx][ny] == 1 :
            snake.append((nx,ny))
            garden[nx][ny] =0
        else :
            snake.pop(0)
            snake.append((nx,ny))
        cnt += 1

print(soultion())