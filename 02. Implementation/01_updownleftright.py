N = int(input())
route = list(input().split())
map = [[0]* N for _ in range(N)]

result = [0,0]

for i in route :
    if result[0] == N-1 and result[1] == N-1  :
        break

    if i == 'L':
        if result[1] == 0 :
            pass
        else :
            result[1] +=1
    elif i == 'R' :
        if result[1] == N-1 :
            pass
        else :
            result[1] +=1
    elif i == 'U' :
        if result[0] == 0 :
            pass
        else :
            result[0] += 1
    elif i == 'D' :
        if result[0] == N-1 :
            pass
        else :
            result[0] +=1

print(result[0]+1 , result[1]+1)

# example
# n = int(input())
# x, y = 1,1
# plans = input().split()
#
# # 로직 사용!!!!
# dx = [0,0,-1,-1]
# dy = [-1,1,0,0]
# move_types = ['L', 'R', 'U', 'D']
#
# for plan in plans :
#     for i in range(len(move_types)) :
#         if plan == move_types[i] :
#             nx = x + dx[i]
#             ny = y + dy[i]
#         if nx < 1 or nx > n or ny < 1 or ny > n :
#             continue
#
#         x,y = nx, ny
#
#     print(x,y)
