from collections import deque

n, l, r = map(int, input().split())
union = []
for _ in range(n) :
    union.append(list(map(int, input().split())))
index = [] # 이동 인구 좌표
cnt = 0 # 인구 이동 횟수
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs() :
    global index,cnt
    for x in range(n) :
        for y in range(n) :
            sum = 0
            q = deque()
            q.append([x,y])
            index.append([x,y])

            while q :
                x,y = q.popleft()
                for i in range(4) :
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx >= 0 and nx < n and ny >= 0 and ny < n :
                        diff = abs(union[x][y] - union[nx][ny])
                        if diff >= l and diff <= r :
                            if [nx,ny] not in index :
                                q.append([nx,ny])
                                index.append([nx,ny])

            if len(index) != 0 :
                for cx, cy in index:
                    sum += union[cx][cy]
                avg = int(sum / len(index))
                for cx, cy in index:
                    union[cx][cy] = avg
                index = []
    print('union', union)
    cnt += 1


def simulate() :
    global cnt
    while True :
        if cnt == 3 :
            break
        bfs()
    print(cnt)
simulate()