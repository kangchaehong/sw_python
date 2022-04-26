def divide(x,y,d1,d2) :
    global total
    location = [[0]*(n+1) for _ in range(n+1)]
    people = [0]*5
    # 경계선 만들기
    location[x][y] = 5
    for i in range(1, d1+1) :
            location[x+i][y-i] = 5
    for i in range(1,d2+1) :
            location[x+i][y+i] = 5
    for i in range(1, d2+1) :
            location[x+d1+i][y-d1+i] = 5
    for i in range(1,d1+1) :
            location[x+d2+i][y+d2-i] = 5

    # 1번 선거구
    for i in range(1,x+d1) :
        for j in range(1, y+1) :
            if location[i][j] == 5 :
                break
            else :
                people[0] += vote[i][j]

    # 2번 선거구
    for i in range(1, x +d2+1):
        for j in range(n, y, -1):
            if location[i][j] == 5:
                break
            else:
                people[1] += vote[i][j]

    # 3번 선거구
    for i in range(x + d1, n+1):
        for j in range(1, y-d1+d2):
            if location[i][j] == 5:
                break
            else:
                people[2] += vote[i][j]

    # 4번 선거구
    for i in range(x + d2+1, n+1):
        for j in range(n, y-d1+d2-1, -1):
            if location[i][j] == 5:
                break
            else:
                people[3] += vote[i][j]

    people[4] = total-sum(people)
    return max(people) - min(people)

n = int(input())
vote = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
# vote = [list(map(int, input().split())) for _ in range(n)] # 1,1 부터 시작인데 처리 못함!! overflow 발생
diff = 1e9

total = 0
for i in range(1, n+1) :
    total+=sum(vote[i])

for x in range(1,n+1) :
    for y in range(1, n+1) :
        for d1 in range(1, n+1) :
            for d2 in range(1, n+1) :
                if x+d1+d2 > n :
                    continue
                if y-d1 <1 or y+d2 > n :
                    continue
                # print(x,y,d1,d2)
                ans = divide(x,y,d1,d2)
                diff = min(diff, ans)
print(diff)