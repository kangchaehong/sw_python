# 갔던 곳에 대한 예외 처리 없음..

row, col = map(int, input().split())
pos = list(map(int, input().split()))

data = []
for i in range(row) :
    data.append(list(map(int, input().split())))

cnt = 1
back = 0
# 방향 북, 동, 남, 서 순서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
directs = [0,1,2,3]
# 현재 위치
nx = pos[0]
ny = pos[1]
nd = pos[2]

data[nx][ny] = 1

while True :
    # 회전 후 가볼 수 있는 칸 찾기
    if data[nx+dx[nd]][ny+dy[nd]] == 1:
        nd = directs[nd-1]
        back += 1
        # 4개 다 막혀있으면
        if back == 4:
            if data[nx + dx[nd - 2]][ny + dy[nd - 2]] == 1:
                break
            else:
                nx += dx[nd - 2]
                ny += dy[nd - 2]
                cnt += 1
            back = 0

    elif data[nx+dx[nd]][ny+dy[nd]] == 0 :
        nx += dx[nd]
        ny += dy[nd]
        cnt += 1
        back = 0
        data[nx][ny] = 1

print(cnt)


