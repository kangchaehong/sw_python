row, col = map(int, input().split())
pos = list(map(int, input().split()))

data = []
for i in range(row) :
    data.append(list(map(int, input().split())))

result = 1
back = 0
cnt =[[0]*col for _ in range(row)]

# 북 동 남 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]
# 현재 방향
dp = pos[2]
cnt[pos[0]][pos[1]] = 1

while True :
    if cnt[pos[0]+dx[dp]][pos[1]+dy[dp]] == 0 and data[pos[0]+dx[dp]][pos[1]+dy[dp]] == 0 :
        pos[0] = pos[0] + dx[dp]
        pos[1] = pos[1] + dy[dp]
        cnt[pos[0]][pos[1]] = 1
        result += 1
        back = 0
    else :
        dp %= 3
        dp = dp-1
        back += 1

    if back == 4 :
        dp = dp-2
        pos[0] = pos[0] + dx[dp]
        pos[1] = pos[1] + dy[dp]
        if data[pos[0]][pos[1]] == 1 :
            break
        else :
            back = 0
            result += 1

print(result)
