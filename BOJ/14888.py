def bfs(cnt, result) :
    global add, sub, mul, div, maxv, minv
    if cnt == n-1 :
        maxv = max(maxv, result)
        minv = min(minv, result)

    else :
        # print(cnt, '//',result)
        if add > 0 :
            add -= 1
            bfs(cnt+1, result+a[cnt+1])
            # print('add', cnt, result)
            add += 1
        if sub > 0 :
            sub-=1
            bfs(cnt+1, result-a[cnt+1])
            # print('sub', cnt, result)
            sub+=1
        if mul > 0:
            mul -= 1
            bfs(cnt+1, result*a[cnt+1])
            # print('mul', cnt, result)
            mul+=1
        if div > 0 :
            div -= 1
            bfs(cnt+1, int(result/a[cnt+1]))
            # print('div', cnt, result)
            div+=1

if __name__ == "__main__" :
    n = int(input())
    a = list(map(int, input().split()))
    add, sub, mul, div = map(int, input().split())
    maxv = -1e9
    minv = 1e9

    bfs(0,a[0])
    print(maxv, minv, sep='\n')

