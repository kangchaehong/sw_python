from collections import deque
from itertools import combinations

n, m = map(int, input().split())
virus = []
blank = []
graph = []
temp = [[0]*m for _ in range(n)]

for i in range(n) :
    graph.append(list(map(int, input().split())))
    for j in range(m) :
        if graph[i][j] == 2 :
            virus.append([i,j])
        elif graph[i][j] == 0 :
            blank.append([i,j])

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs() :
    for i in range(n) :
        for j in range(m) :
            temp[i][j] = graph[i][j]

    q = deque(virus)
    while q :
        x, y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < n and nx >= 0 and ny < m and ny >= 0 :
                if temp[nx][ny] == 0 :
                    temp[nx][ny] = 2
                    q.append((nx, ny))
    count = 0
    for i in range(n) :
        for j in range(m) :
            if temp[i][j] == 0:
                count += 1
    return count

def comb(arr, n) :
    result = []
    if n > len(arr) :
        return arr
    if n == 1 :
        for i in arr:
            result.append([i])
    elif n > 1 :
        for i in range(len(arr) - n + 1) :
            for j in comb(arr[i+1:], n-1) :
                result.append([arr[i]]+j)
    return result


answer = 0
result = comb(blank, 3)
for data in result:
    for x, y in data :
        graph[x][y] = 1
    answer = max(answer, bfs())
    for x, y in data :
        graph[x][y] = 0

print(answer)