from collections import deque

n, l, r = map(int, input().split())
# 각 나라 인구 수
people = []
for _ in range(n) :
    people.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y) :
    q=deque()
    q.append((x,y))
    visit[x][y] = True
    union = [(x,y)] # 연합된 국가 담기
    sum_p = people[x][y]

    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            # 방문했던 좌표면 지나감
            if nx < 0 or nx >= n or ny < 0 or ny >= n :
                continue
            if visit[nx][ny] == True :
                continue
            if l <= abs(people[nx][ny]-people[x][y]) <=r :
                union.append((nx,ny))
                visit[nx][ny] = True
                q.append((nx,ny))
                sum_p += people[nx][ny]

    for x, y in union :
        people[x][y] = int(sum_p/len(union))

    return len(union)

result = 0
while True : # 1. 인구 이동이 없을때까지 반복
    visit = [[0] * n for _ in range(n)] # 방문했는지
    flag = False # 인구 이동 존재 유무
    for i in range(n) :
        for j in range(n) :
            if not visit[i][j] : # 방문한 적 없으면
                if bfs(i,j) > 1 :
                    flag = True
    if not flag :
        break
    result += 1 # 인구 이동 시 +1

print(result)