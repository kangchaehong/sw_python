# 입력부
n = int(input())
k = int(input())
apple = [[0] * (n+1) for _ in range(n+1)]
for i in range(k) :
    x, y = map(int, input().split())
    apple[x][y] = 1

l = int(input())
rotate = []
for i in range(l) :
    count, direct = input().split()
    rotate.append((int(count), direct))

# 실행부
def ro(dr,dir) :
    if dir == 'D' :
        dr = (dr+1)%4
    else :
        dr = (dr-1)%4
    return dr

def simulate() :
    # 변수부
    snake = [(1, 1)]
    index = 0
    dr = 0  # 방향 인덱스
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오른쪽 방향 바라보고 시계방향으로
    cnt = 0
    while True :
        nx = snake[0][0] + d[dr][0]
        ny = snake[0][1] + d[dr][1]
        if 1 <= nx and nx <= n and 1<=ny and ny <=n and ((nx, ny) not in snake) :
            if apple[nx][ny] == 0 :
                snake.insert(0,(nx, ny))
                snake.pop(-1)
            if apple[nx][ny] == 1 :
                snake.insert(0,(nx, ny))
        # if nx > n or nx < 0 or ny > n or ny < 0 :
        #     cnt-=1
        #     break
        # if (nx, ny) in snake:
        #     break
        else :
            cnt += 1
            break
        cnt += 1
        # print(rotate)
        if len(rotate) != 0 and rotate[0][0] == cnt :
            c, dir = rotate.pop(0)
            dr = ro(dr, dir)
        #     print('dr', dr)
        # print(snake)
        # if apple[nx][ny] != 1 :
        #     if len(snake) >= 1 :
        #         snake.pop(-1)
        # snake.insert(0, (nx,ny))

    return cnt

print(simulate())