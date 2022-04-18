from collections import deque
# 입력부
n, k = map(int, input().split())
addict = []
virus = []
virus = [0] * k
cnt = 0
for i in range(n) :
    addict.append(list(map(int, input().split())))
    for j in range(n) :
        if addict[i][j] != 0 :
            virus.append([addict[i][j], i,j, cnt])
            # virus[addict[i][j]-1] = ([addict[i][j], i, j, cnt])
s,x,y = map(int, input().split())
virus.sort()
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 실행부
def bfs() :
    q = deque(virus)
    while q :
        val,a,b,cnt = q.popleft()
        if cnt == s :
            break
        for i in range(4) :
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < n and nx >= 0 and ny < n and ny >= 0:
                if addict[nx][ny] == 0 :
                    addict[nx][ny] = val
                    q.append((val, nx, ny,cnt+1))


bfs()
print(addict[x-1][y-1])


