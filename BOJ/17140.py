cnt = 0
newa = []
b = []

# R 연산 : 행 >= 열
def R() :
    maxlen = 0
    temp_matrix = []
    for i in range(len(a)) :
        numbers = set(a[i])
        temp = []
        for num in numbers :
            if num == 0 :
                continue
            temp.append([num, a[i].count(num)])
        maxlen = max(maxlen, len(temp)*2)
        temp_matrix.append(temp)

    for i in range(len(temp_matrix)) :
        temp_matrix[i].sort(key=lambda x : (x[1],x[0]))

    for i in range(len(temp_matrix)) :
        templst = []
        for j in range(len(temp_matrix[i])) :
            templst.append(temp_matrix[i][j][0])
            templst.append(temp_matrix[i][j][1])
        templst.extend([0]*(maxlen-len(templst)))
        if len(templst) > 100 :
            templst = templst[:100]
        a[i] = templst

if __name__ == "__main__" :
    r, c, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(3)]
    time = 0

    while time < 101 :
        if r-1 < len(a) and c-1 < len(a[0]) :
            if a[r-1][c-1] == k:
                print(time)
                break

        if len(a) >= len(a[0]):
            R()
        else :
            a = list(map(list, zip(*a)))
            R()
            a = list(map(list, zip(*a)))
        time+=1

    else :
        print(-1)