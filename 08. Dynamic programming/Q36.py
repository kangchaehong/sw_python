
def edit_func(a,b) :
    n = len(a)
    m = len(b)
    # dp table 초기화
    d = [[0]*(m+1) for _ in range(n+1)]
    # dp 테이블 초기화 설정
    for i in range(1,n+1) :
        d[i][0]= i
    for j in range(1, m+1) :
        d[0][j] = j

    for i in range(1,n+1) :
        for j in range(1, m+1) :
            # 만약 단어가 같다면
            if a[i-1] == b[j-1] :
                d[i][j] = d[i-1][j-1]
            # 같지 않다면 왼쪽 위 > 교체, 위 > 추가, 왼쪽 > 삭제
            else :
                d[i][j] = 1 + min(d[i-1][j-1], d[i][j-1], d[i-1][j])
    return d[n][m]

a = input()
b = input()
print(edit_func(a,b))

