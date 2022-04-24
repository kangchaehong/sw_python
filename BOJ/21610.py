n, m = map(int,input().split())
basket = [list(map(int, input().split())) for _ in range(n)]
move=[list(map(int, input().split())) for _ in range(m)]

dx = [0,0,-1,-1,-1,0,1,1,1]
dy = [0,-1,-1,0,1,1,1,0,-1]

cloud = [(n-1,0),(n-1,1),(n-2,0),(n-2,1)]

for a in range(m) :
    new_cloud = []
    for x,y in cloud :
        for i in range(move[a][1]) :
            x += dx[move[a][0]]
            y += dy[move[a][0]]
        if x>=n or x<0 or y<0 or y>=n :
            x = (x+n)%n
            y = (y+n)%n
        new_cloud.append((x, y))
    for x,y in new_cloud :
        basket[x][y] += 1

    for x,y in new_cloud :
        plus = 0
        for i in range(2,9,2) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=0 and nx < n and ny>=0 and ny <n :
                if basket[nx][ny] != 0 :
                    plus +=1
        basket[x][y] += plus

    cloud = []
    for i in range(n) :
        for j in range(n) :
            if basket[i][j] >= 2 and (i,j) not in new_cloud :
                cloud.append((i,j))
                basket[i][j] -= 2
sum = 0
for i in range(n) :
    for j in range(n) :
        sum+=basket[i][j]
print(sum)