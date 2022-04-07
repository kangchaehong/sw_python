from collections import deque

n, m = map(int, input().split())
virus = []
coord = []
temp = [[0]*m for i in range(n)]
check_array = []

for i in range(n) :
    virus.append(list(map(int, input().split())))
    for j in range(m) :
        if virus[i][j] == 0:
            coord.append([i,j])

def comb(arr, n) :
    result = []
    if n > len(arr):
        return arr
    if n == 1 :
        for i in range(len(arr)):
            result.append([arr[i]])
    elif n > 1 :
        for i in range(len(arr)-n+1) :
            for j in comb(arr[i+1:], n-1) :
                result.append([arr[i]]+j)
    return result
# print(comb(coord,3))

dx = [1,-1,0,0]
dy = [0,0,-1,1]


def dfs(x,y) :
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < n and nx >= 0 and ny < m and ny >= 0 :
            if temp[nx][ny] == 0 :
                temp[nx][ny] = 2
                dfs(nx,ny)

def check() :
    cnt = 0
    for i in range(n) :
        for j in range(m) :
            if temp[i][j] == 0 :
                cnt += 1
    check_array.append(cnt)


result = comb(coord, 3)
for i in result :
    for j in i :
        virus[j[0]][j[1]] = 1

    for c in range(n) :
        for d in range(m) :
            temp[c][d] = virus[c][d]

    for a in range(n) :
        for b in range(m) :
            if virus[a][b] == 2 :
                dfs(a,b)
    check()
    for j in i :
        virus[j[0]][j[1]] = 0

print(max(check_array))