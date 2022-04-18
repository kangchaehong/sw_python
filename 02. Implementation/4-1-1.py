n = int(input())
moves = list(map(str, input().split()))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

direct = ['L','R','U','D']

x, y = 1,1

for move in moves :
    # 이 부분!!!
    for i in range(len(direct)) :
        if move == direct[i] :
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or nx > 5 or ny < 1 or ny > 5 :
        continue

    x, y = nx, ny

print(x,y)