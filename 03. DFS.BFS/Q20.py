from collections import deque

n = int(input())
school = []
teacher = []
obstacle = []
temp = [[0] * n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n) :
    school.append(list(input().split()))
    for j in range(n) :
        if school[i][j] == 'T' :
            teacher.append((i,j))
        elif school[i][j] == 'X' :
            obstacle.append((i,j))

def bfs() :
    q = deque(teacher)
    for i in range(n) :
        for j in range(n) :
            temp[i][j] = school[i][j]
    while q :
        x, y = q.popleft()
        for i in range(4):
            temp_x, temp_y = x,y
            while True :
                nx = temp_x + dx[i]
                ny = temp_y + dy[i]
                # print(temp)
                if nx < n and nx >= 0 and ny < n and ny >=0 :
                    if temp[nx][ny] == 'X' :
                        temp[nx][ny] = 'T'
                        # q.append((nx,ny))
                    elif temp[nx][ny] == 'S' :
                        return False
                    elif temp[nx][ny] == 'O' :
                        break
                    temp_x, temp_y = nx, ny
                else:
                    break
    return True

def comb(obstacle, n) :
    result = []
    if len(obstacle) < n :
        return obstacle
    if n == 1 :
        for i in obstacle :
            result.append([i])
    elif n > 1 :
        for i in range(len(obstacle)-n+1) :
            for j in comb(obstacle[i+1:], n-1) :
                result.append([obstacle[i]]+j)
    return result

check = False
result_ob = comb(obstacle, 3)
for i in result_ob:
    for x, y in i:
        print(x,y)
        school[x][y] = 'O'
    if bfs():
        check = True
        break
    for x, y in i:
        school[x][y] = 'X'

if check :
    print("YES")
else :
    print("NO")

# for i in range(length) :
#     for j in result :
#         for k in len(result[j]) :
#             temp[i][j]

# def dfs(x,y) :
#     for i in range(4) :
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if nx < n and nx >= 0 and ny < n and ny >=0 :
#             if school[nx][ny] == 'X' :
#                 dfs(nx, ny)
#             if school[nx][ny] == 'S' :
#                 hide = 'NO'
#                 break
#             if school[nx][ny] == 'O' :
#                 break
#     hide = 'YES'
#     return hide
# print(dfs(teacher[0][0], teacher[0][1]))
# print(hide)

