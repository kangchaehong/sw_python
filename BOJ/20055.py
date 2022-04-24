from collections import deque

n, k = map(int,input().split())
container = deque(list(map(int, input().split())))
robot = deque([0]*n)

step = 0

while True :
    step += 1
    # step1 벨트, 로봇 이동
    container.rotate(1)
    robot.rotate(1)
    robot[-1] = 0

    # step2 로봇 이동 (끝에서 부터 확인! 먼저 들어온 것 부터, n-1에서 나가니까 n-2부터 탐색!)
    if robot :
        for i in range(n-2, -1, -1) :
            if robot[i] == 1 and robot[i+1] == 0 and container[i+1] >=1 :
                container[i+1] -= 1
                robot[i] = 0
                robot[i+1] = 1
        robot[-1] = 0

    # step3 로봇 올리기
    if robot[0] == 0 and container[0]!=0 :
        robot[0] = 1
        container[0] -= 1

    # step4 count 세기
    cnt0 = 0
    if container.count(0) >=k :
        break

print(step)