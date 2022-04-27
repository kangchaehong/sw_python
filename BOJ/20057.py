
# 허리케인 이동 방향
delta = [(0,-1),(1,0),(0,1),(-1,0)]

def rotate_90(arr) :
    new_arr = list(reversed(list(zip(*arr))))
    return new_arr

p = [[0, 0, 0.02, 0, 0],
	[0, 0.1, 0.07, 0.01, 0],
    [0.05, 0, 0, 0, 0],
    [0, 0.1, 0.07, 0.01, 0],
    [0, 0, 0.02, 0, 0]]

# 허리케인 방향에 맞춰 비율 바꾸기
p1 = rotate_90(p)
p2 = rotate_90(p1)
p3 = rotate_90(p2)
proportions = [p,p1,p2,p3]
alpha = [(2,1),(3,2),(2,3),(1,2)]

# 허리케인 이동 + 모래 이동
def solution():
    # (0) 초기 조건
    outer_sand = 0
    tx = hx # 토네이도 위치 인덱스 -> 시작 지점부터 시작
    ty = hy
    cur = 0 # 현재 토네이도 방향
    turn = 2 # 토네이도 방향 바꾸는 지표
    now = 0 # 토네이도 직선 길이
    proportion = proportions[0] # 토네이도 방향에 따른 비율 배열

    # (1) 토네이도가 종료 될때까지 이동 -> 모래 이동 -> 토네이도 방향 바꾸기
    while not (tx == 0 and ty == 0) :
        # (1-1) 토네이도 이동
        tx += delta[cur][0]
        ty += delta[cur][1]
        now += 1 # 토네이도 길이 추가
        sand = data[tx][ty]
        data[tx][ty] = 0
        left = sand # 모래 이동 후 남은 모래

        # (1-2) propagation의 y 위치와 data 토네이도 위치 일치시켜서 모래 정보 업데이트하기
        for i in range(5) :
            for j in range(5) :
                now_sand = int(sand*proportion[i][j])
                left -= now_sand
                # 2 를 빼주는 이유는 회전 좌표, 토네이도 좌표의 차이 구하려고!
                if 0 <= tx+i-2 < n and 0<=ty+j-2<n :
                    data[tx+i-2][ty+j-2] += now_sand
                else :
                    outer_sand += now_sand

        if 0 <= tx + alpha[cur][0] -2 < n and 0 <= ty + alpha[cur][1]-2 < n :
            data[tx+alpha[cur][0]-2][ty+alpha[cur][1]-2] += left
        else :
            outer_sand += left

        # (1-3) 토네이도 방향 바꾸기
        # 2세트당 길이 1씩 증가 -> 정해진 길이일 경우 회전
        # 2세트당 길이 1씩 증가하므로 2세트 종료 시 +2 해주어서 각 세트마다 1씩 더 증가할 수 있도록  update
        if now == turn // 2 or now == turn :
            cur = (cur+1) % 4
            proportion = proportions[cur]
            if now == turn :
                now = 0
                turn += 2

    print(outer_sand)
    return

# main
n = int(input())
hx = hy = n//2 # 허리케인 시작 지점
data = []
for _ in range(n) :
    data.append(list(map(int, input().split())))

solution()