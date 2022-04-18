n = int(input())
group = list(map(int, input().split()))
# 작은 것부터 정렬
group.sort()
cnt, result = 0, 0
for i in range(n) :
    cnt += 1
    if group[i] == cnt :
    # if group[i] <= cnt :
        result += 1
        cnt = 0
print(result)