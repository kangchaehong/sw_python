n= int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1

for i in range(n) :
    if coins[i] > target :
        break
    else :
        target += coins[i]
print(target)