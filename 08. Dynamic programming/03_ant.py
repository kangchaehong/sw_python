n = int(input())
factory = list(map(int, input().split()))

sum = 0
max_v = -1e9
for i in range(n) :
    for j in range(i+1, n) :
        if j >= n-1 :
            break
        sum = factory[i] + factory[j+1]
        max_v = max(sum, max_v)
print(max_v)

# dp
n = int(input())
factory = list(map(int, input().split()))

d = [0] * 100

d[0] = factory[0]
d[1] = max(factory[0], factory[1])
for i in range(2, n) :
    d[i] = max(d[i-1], d[i-2]+factory[i])
print(d[n-1])