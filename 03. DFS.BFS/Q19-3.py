n = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_val = 1e9
max_val = -1e9

def dfs(i, now) :
    global min_val, max_val, add, sub, mul, div
    if i == n :
        min_val = min(min_val, now)
        max_val = max(max_val, now)
    else :
        if add > 0 :
            add -= 1
            dfs(i+1, now+num[i])
            add += 1
        elif sub > 0 :
            sub -= 1
            dfs(i+1, now-num[i])
            sub += 1
        elif mul > 0 :
            mul -= 1
            dfs(i+1, now*num[i])
            mul += 1
        elif div > 0 :
            div -= 1
            dfs(i+1, int(now//num[i]))
            div += 1

dfs(1, num[0])

print(max_val)
print(min_val
      )