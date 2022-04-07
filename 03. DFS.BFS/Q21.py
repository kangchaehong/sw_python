n, l, r = map(int, input().split())
people, data = [], []
for _ in range(n) :
    people.append(list(map(int, input().split())))

sum, count, total = 0, 0, 0
data = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def check(x,y) :
    global people,sum, data
    for i in range(n) :
        for j in range(n) :
            people[i][j]
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        if [x, y] in data :
            continue
        if nx < n and nx >=0 and ny < n and ny >= 0 :
            sub = abs(people[nx][ny]-people[x][y])
            if sub >= l and sub <= r :
                data.append([x,y])
                break

def dfs() :
    global count, sum, total
    for i in range(n) :
        for j in range(n):
            check(i,j)
    for in_x, in_y in data :
        sum += people[in_x][in_y]
        count +=1
    for in_x, in_y in data :
        people[in_x][in_y] = int(sum / count)
    total += 1
    return total

print(dfs())


