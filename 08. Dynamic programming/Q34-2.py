n = int(input())
arr = list(map(int, input().split()))
d = [1]*n
for i in range(n-1) :
    for j in range(i+1,n) :
        if arr[i] > arr[j] :
            d[j] = max(d[j], d[i]+1)
            print('i,j',i,j)
            print(d)
print(n-max(d))


