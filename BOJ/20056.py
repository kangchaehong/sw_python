n, m, k = map(int, input().split())
magic = [[[] for _ in range(n)] for _ in range(n)]
info = []
for _ in range(m) :
    x,y,m,s,d = map(int,input().split())
    info.append([x-1,y-1,m,s,d])

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

# x,y,질량,속력,방향
for _ in range(k) :
    # 이동
    while info :
        x,y,m,s,d = info.pop(0)
        nx = ((x + (dx[d])*s)+n) % n
        ny = ((y + (dy[d])*s)+n) % n
        magic[nx][ny].append([m, s, d])

    for i in range(n) :
        for j in range(n) :
            # 길이가 2개인 경우
            if len(magic[i][j]) > 1 :
                change_m = 0
                change_s = 0
                temp_d = 0
                length = len(magic[i][j])
                while magic[i][j] :
                    _m, _s, _d = magic[i][j].pop(0)
                    change_m += _m
                    change_s += _s
                    temp_d += _d % 2
                change_m = int(change_m / 5)
                change_s = int(change_s / length)
                if temp_d == 0 or temp_d == length :
                    change_d = [0,2,4,6]
                else :
                    change_d = [1,3,5,7]

                if change_m != 0 :
                    for h in range(len(change_d)) :
                        info.append([i,j,change_m, change_s, change_d[h]])

            # 길이가 1개인 경우
            if len(magic[i][j]) == 1 :
                m,s,d = magic[i][j].pop(0)
                info.append([i,j,m,s,d])

print(sum([inf[2] for inf in info]))