n, m = map(int, input().split())
w = list(map(int, input().split()))

pos = 0
cnt = 0
for j in range(len(w)-1) :
    for i in range(j+1,len(w)) :
        if w[j] != w[i] :
            cnt += 1
print(cnt)

# example
array = [0]*11
for i in w :
    array[i] += 1

for i in range(1, m+1) :
    n -= array[i]
    cnt += array[i] * n

print(cnt)