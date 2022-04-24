def placement() :
    for a in range(n*n) :
        table = like_table[a][0]
        likes = like_table[a][1:]
        temp = []
        for i in range(n) :
            for j in range(n) :
                # print('i,j', i,j)
                if tables[i][j] == 0 :
                    blank = 0
                    like = 0
                    for k in range(4) :
                        nx = i+dx[k]
                        ny = j+dy[k]
                        if nx >=0 and nx<n and ny>=0 and ny<n:
                            if tables[nx][ny] == 0 :
                                blank += 1
                            if tables[nx][ny] in likes :
                                like += 1
                    temp.append((like,blank,i,j))
                    # print(a, temp)
        temp.sort(key=lambda x :(-x[0], -x[1], x[2],x[3]))
        # print(temp)
        tables[temp[0][2]][temp[0][3]] = table
        # print(tables)
    cal(tables, like_table)

def cal(tables, like_table) :
    like_table.sort()
    sum = 0
    for i in range(n) :
        for j in range(n) :
            cnt = 0
            for k in range(4) :
                nx = i + dx[k]
                ny = j + dy[k]
                if nx>=0 and nx<n and ny>=0 and ny <n :
                    if tables[nx][ny] in like_table[tables[i][j]-1] :
                        cnt +=1
            if cnt != 0:
                sum += 10**(cnt-1)
    print(sum)

if __name__ == "__main__"  :
    n = int(input())
    like_table = [list(map(int, input().split())) for _ in range(n*n)]
    tables = [[0] * n for _ in range(n)]

    # 방향 벡터
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    # 실행함수
    placement()