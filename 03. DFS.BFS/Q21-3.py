from collections import deque

# 입력부
n,l,r = map(int, input().split())
union = []
for _ in range(n) :
    union.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y) :
    move_q = deque()
    q.append([x,y])
    c[x][y] = 1
    people,cnt = 0,0 # cnt : 나눌 총 개수
    while q :
        x,y = q.popleft()
        move_q.append([x,y])
        people += union[x][y]
        cnt += 1
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >=0 and nx <n and ny >= 0 and ny < n and not c[nx][ny]:
                if l <= abs(union[nx][ny]-union[x][y]) <= r :
                    c[nx][ny] = cnt
                    q.append([nx,ny])
    print('cnt', cnt)
    print('c', c)
    print(union)
    while move_q :
        x,y = move_q.popleft()
        union[x][y] = people // cnt

    if cnt == 1 :
        return 0
    return 1

ans = 0
while True :
    q=deque()
    c=[[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n) :
        for j in range(n) :
            if not c[i][j] :
                cnt+=bfs(i,j)

    if not cnt :
        break
    ans +=1

print(ans)