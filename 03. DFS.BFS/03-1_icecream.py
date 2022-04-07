n, m = map(int, input().split())
ice = []
count = 0
for i in range(n) :
    ice.append(list(map(int, input())))

def bfs(x,y):
    if x >= n or x < 0 or y >=m or y < 0 :
        return False

    if ice[x][y] == 0 :
        return False

    else :
        bfs(x-1,y)
        bfs(x,y-1)
        bfs(x+1,y)
        bfs(x,y+1)
        return True
    return False

for i in range(n) :
    for j in range(m) :
        if bfs(i,j) :
            count += 1

print(count)
