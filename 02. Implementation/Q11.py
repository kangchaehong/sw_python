n = int(input())
k = int(input())
apples =[[0]*(n+1) for _ in range(n+1)]
l_num = []

for _ in range(k) :
    a,b = map(int, input().split())
    apples[a][b] = 1

l = int(input())
for _ in range(l) :
    x, c = input().split()
    l_num.append((int(x), c))

# 동 남 서 북 시계 방향
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, 1]
#
# def turn(dc, c) :
#     if c == 'L' :
#         dc -= 1
#         dc %= 3
#     else :
#         dc += 1
#         dc %= 3
#     return dc

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(dc, c) :
    if c == "L" :
        dc = (dc -1) % 4
    else :
        dc = (dc +1) % 4
    return dc

def simulate() :
    # 머리 위치
    head_x = 1
    head_y = 1
    apples[head_x][head_y] = 2

    # 현재 방향
    dc = 0
    # 다음 회전 정보
    index = 0
    # count
    cnt = 0
    # 뱀이 차지하는 위치 정보 -> 꼬리가 앞쪽
    q = [(head_x,head_y)]

    while True :
        nx = head_x+dx[dc]
        ny = head_y+dy[dc]

        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and apples[nx][ny] != 2 :
            # 사과 안 만난 경우
            if apples[nx][ny] == 0 :
                apples[nx][ny] = 2
                q.append((nx, ny))
                tail_x, tail_y = q.pop(0)
                apples[tail_x][tail_y] = 0
            # 사과 만난 경우
            if apples[nx][ny] == 1:
                apples[nx][ny] = 2
                q.append((nx, ny))
        else :
            cnt += 1
            break
        head_x = nx
        head_y = ny
        cnt += 1

        if index < l and cnt == l_num[index][0] :
            dc = turn(dc, l_num[index][1])
            index += 1

    return cnt

print(simulate())
