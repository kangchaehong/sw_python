n = int(input())
tri = []
for i in range(n) :
    tri.append(list(map(int, input().split())))

for i in range(n-2,-1,-1):
    for j in range(0, i+1) :
        tri[i][j] = tri[i][j] + max(tri[i+1][j], tri[i+1][j+1])
print(tri[0][0])