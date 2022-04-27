n = int(input())
hx = hy = n//2 # 허리케인 시작 지점
sand = []
for _ in range(n) :
    sand.append(list(map(int, input().split())))



def rotate_90(arr) :
    new_arr = list(reversed(list(zip(*arr))))
    print(new_arr)
    return new_arr

p = [[0, 0, 0.02, 0, 0],
	[0, 0.1, 0.07, 0.01, 0],
    [0.05, 0, 0, 0, 0],
    [0, 0.1, 0.07, 0.01, 0],
    [0, 0, 0.02, 0, 0]]

# 허리케인 방향에 맞춰 비율 바꾸기
p1 = rotate_90(p)
p2 = rotate_90(p1)
p3 = rotate_90(p2)
proportion = [p,p1,p2,p3]
alpha = [(2,1),(3,2),(2,3),(1,2)]

# 허리케인 이동 + 모래 이동
def solution():
    # 초기 조건


