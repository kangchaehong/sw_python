n = int(input())
coins = list(map(int, input().split()))
coins.sort()
cnt = 1
for coin in coins :
    if cnt < coin :
        break
    cnt += coin
print(cnt)