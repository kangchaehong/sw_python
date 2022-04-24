def game() :
    # 초기값 설정
    snake = [(1, 1)]
    dir = 0 # 회전 방향
    dircnt = 0 # 회전 배열 카운트
    cnt = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while True :
        # print('1', snake)
        if len(change) > dircnt and change[dircnt][0] == str(cnt) :
            if change[dircnt][1] == 'D' :
                dir = (dir+1)%4
            else :
                dir = (dir - 1) % 4
            dircnt+=1

        nx = snake[-1][0] + dx[dir]
        ny = snake[-1][1] + dy[dir]
        if nx < 1 or ny > n or nx >n or ny < 1 or (nx,ny) in snake :
            cnt += 1
            break
        else :
            if board[nx][ny] == 1 :
                snake.append((nx,ny))
                board[nx][ny] = 0
            elif board[nx][ny] == 0 :
                snake.append((nx,ny))
                snake.pop(0)
            # print('2', snake)
        cnt += 1
    return cnt

if __name__ == "__main__" :
    n = int(input())
    board=[[0]*(n+2) for _ in range(n+2)]

    k = int(input())
    for _ in range(k) :
        a,b = map(int, input().split())
        board[a][b] = 1
    l = int(input())
    change = [list(map(str, input().split())) for _ in range(l)]

    print(game())