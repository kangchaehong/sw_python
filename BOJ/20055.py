n, k = map(int,input().split())
container = list(map(int, input().split()))
robot = [0]*len(container)
# 초기 up down 위치
up = 0
down = n-1
# 0 카운트
cnt0 = 0
step = 0
while True :
    cnt0 = 0
    print('up',up,'down',down)
    if container[up] >= 1 and robot[up] == 0:
        robot[up] = 1
        container[up] -= 1
    print('c', container)
    if robot[down] == 1 :
        robot[down] = 0
    print('r', robot)

    # 회전
    if up == 0 :
        up = len(container) -1
    else :
        up -= 1
    if down == 0 :
        down = len(container) - 1
    else :
        down -= 1

    for i in range(2*n) :
        if container[i] == 0 :
            cnt0 += 1
    if cnt0 == k :
        break
    step += 1
print(step)