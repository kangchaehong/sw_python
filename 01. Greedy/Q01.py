n = int(input())
a = list(map(int, input().split()))

a.sort()
result = 0
cnt = 1

for i in a :
    if i == cnt :
        result += 1
        cnt = 1
    else :
        cnt +=1
        continue

print(result)
