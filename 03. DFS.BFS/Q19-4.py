n = int(input())
a = list(map(int, input().split()))
count = list(map(int, input().split()))

add, sub, mul, div = count[0], count[1], count[2], count[3]
maxv = -1e9
minv = 1e9
cnt = 1
result = a[0]

def dfs(cnt, value) :
    global add, sub, mul, div, result, minv, maxv

    if cnt == n :
        minv = min(minv, value)
        maxv = max(maxv, value)

    else :
        if add > 0 :
            add -= 1
            dfs(cnt+1,value+a[cnt])
            add += 1

        if sub > 0 :
            sub -= 1
            dfs(cnt+1, value-a[cnt])
            sub += 1

        if mul > 0 :
            mul -= 1
            dfs(cnt+1,value*a[cnt])
            mul += 1

        if div > 0 :
            div -= 1
            dfs(cnt+1, int(value/a[cnt]))
            div += 1

dfs(cnt, result)
print(maxv)
print(minv)