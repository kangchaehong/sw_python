n = int(input())
for i in range(n) :
    n, m = map(int, input().split())
    a=list(map(int, input().split()))

    d =[]
    cnt = 0
    for _ in range(n) :
        d.append(a[cnt:m+cnt])
        cnt += m

    for j in range(1,m) :
        for i in range(n) :
            if i==0 : left_up = 0
            else : left_up = d[i-1][j-1]
            if i == n-1 : left_down = 0
            else : left_down = d[i+1][j-1]
            left = d[i][j-1]
            d[i][j] = d[i][j] + max(left, left_down, left_up)

    result = 0
    for i in range(n) :
        result = max(result, d[i][m-1])
    print(result)