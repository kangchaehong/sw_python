from collections import deque

n, k = map(int, input().split())
graph = []
virus = []

for i in range(n) :
    graph.append(list(map(int, input().split())))
    for j in range(n) :
        if graph[i][j] != 0:
            virus.append([graph[i][j],0, i, j])
s, x, y = map(int, input().split())
virus.sort()


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs() :
    q = deque(virus)

    while q :
        vi, time, a, b = q.popleft()
        if time == s :
            break

        for i in range(4) :
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < n and nx >= 0 and ny < n and ny >= 0 :
                if graph[nx][ny] == 0 :
                    graph[nx][ny] = vi
                    q.append((vi, time+1, nx, ny))

bfs()
print(graph[x-1][y-1])