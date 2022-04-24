def calc() :
    global maxv
    count = 0
    for i in range(n) :
        for j in range(m) :
            if temp[i][j] == 0 :
                count += 1

    maxv = max(count, maxv)
    # print(maxv)

def viruspro(vix, viy):
    for i in range(4) :
        nvix = vix + dx[i]
        nviy = viy + dy[i]
        if nvix >= 0 and nvix < n and nviy >=0 and nviy < m and temp[nvix][nviy] == 0 :
            temp[nvix][nviy] = 2
            viruspro(nvix, nviy)


def wall(cnt) :
    global temp
    if cnt == 3 :
        # print('wall>',temp)
        for i in range(n):
            for j in range(m):
                temp[i][j] = lab[i][j]
        for vix, viy in virus :
            viruspro(vix,viy)
        # print('pro',temp)
        calc()
        return

    for i in range(n) :
        for j in range(m) :
            if lab[i][j] == 0 :
                lab[i][j] = 1
                wall(cnt+1)
                lab[i][j] = 0


if __name__ == "__main__" :
    n, m = map(int,input().split())
    lab = []
    virus = []
    temp = [[0]*m for _ in range(n)]
    for i in range(n) :
        lab.append(list(map(int, input().split())))
        for j in range(m) :
            if lab[i][j] == 2 :
                virus.append([i,j])
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]
    maxv = -1e9

    wall(0)
    print(maxv)