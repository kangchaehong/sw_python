n = int(input())
foods = list(map(int, input().split()))

d = [0] * 100
d[0] = foods[0]
d[1] = foods[1]
#
# for i in range(n) :
#     for j in range(i+2, n):
#         d[i] = max(foods[i], foods[i+j] + foods[i])

for i in range(2,n) :
    d[i] = max(d[i-1], d[i-2] + foods[i])
print(max(d))
