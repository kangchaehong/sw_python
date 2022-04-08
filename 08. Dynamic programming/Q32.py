n = int(input())
array = []
for _ in range(n) :
    array.append(list(map(int, input().split())))

d = [[0]*n for _ in range(n)]
d[0][0] = array[0][0]

for i in range(1,n) :
    for j in range(len(array[i])) :
        # 왼쪽 대각선
        if j-1 < 0 : left_down = 0
        else : left_down = d[i-1][j-1]
        # 오른쪽 대각선
        if j+1 > len(array[i-1]) : right_down = 0
        else : right_down = d[i-1][j]
        d[i][j] = array[i][j] + max(left_down, right_down)
print(max(d[-1]))