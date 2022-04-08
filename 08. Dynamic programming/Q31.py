t = int(input())
for a in range(t) :
    n, m = map(int,input().split())
    a = list(map(int, input().split()))
    # dp 테이블 초기화
    d = []
    index = 0
    for i in range(n) :
        d.append(a[index:index+m])
        index += m

    for j in range(1, m) :
        for i in range(n) :
            # 왼쪽 위에서 오는 경우
            if i == 0 : left_up = 0
            else : left_up = d[i-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if i == n-1 : left_down = 0
            else : left_down = d[i+1][j-1]
            # 왼쪽에서 오는 경우
            left = d[i][j-1]
            d[i][j] = d[i][j] + max(left, left_up, left_down)
    result = 0
    for i in range(n) :
        result = max(result, d[i][m-1])
    print(result)

print(gold)