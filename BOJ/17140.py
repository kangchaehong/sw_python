cnt = 0
newa = []
b = []

# R 연산 : 행 >= 열
def R(a) :
    cnt = 0
    maxlen = 0
    for alist in a :
        del alist[0]
        for value in alist :
            for k in range(len(b)) :
                if b[k][0] == value :
                    # print(b)
                    b[k][1] += 1
                    break
            else :
                b.append([value,1])
        b.sort(key=lambda x : (x[1],x[0]))
        newa.append([])

        # 입력
        for i in range(len(b)) :
            for j in range(len(b[0])) :
                newa[cnt].append(b[i][j])
            maxlen = max(maxlen, len(newa[cnt]))
        cnt += 1

        # 0 넣어주기
        for i in range(len(newa)) :
            if len(newa[i]) < maxlen :
                for _ in range(maxlen-len(newa[i])) :
                    newa[i].append(0)
        b = []
    return newa

def main() :
    time = 0
    r, c, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(3)]
    while True :
        if r < len(a) and c < len(a[0]):
            if a[r][c] == k:
                return time
        else :
            if len(a) >= len(a[0]):
                a = R(a)
            else :
                a = list(map(list, zip(*a)))
                a = R(a)
                a = list(map(list, zip(*a)))
            time+=1
            if time > 100 :
                return -1
    print(time)
main()