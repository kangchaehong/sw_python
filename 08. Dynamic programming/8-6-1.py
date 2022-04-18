n = int(input())
foods = list(map(int, input().split()))

d = [0] * 100
d[0] = foods[0]
d[1] = max(foods[0], foods[1])
for i in range(2,n) :
    d[i] = max(d[i-2]+foods[i], d[i-1])

print(d[n-1])