n, m = map(int, input().split())
ball = list(map(int, input().split()))
ball.sort()

cnt = 0
w = 1

for i in range(n-1) :
    if ball[i] != ball[i+1] :
        cnt += (len(ball) - (i+1))*w
        w = 1
    else :
        w += 1

print(cnt)
