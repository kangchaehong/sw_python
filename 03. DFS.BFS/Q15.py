from collections import deque

n, m, k, x = map(int, input().split())
dist = [[] for _ in range(n+1)]

# 모든 도로 정보 받기!!!
for _ in range(m) :
    a,b = map(int, input().split())
    dist[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0 # 출발 도시 거리는  0으로 설정

q = deque([x])
while q :
    a = q.popleft()
    for i in dist[a] :
        if distance[i] == -1 :
            distance[i] = distance[a] + 1
            q.append(i)

check = False
for i in range(1, n+1) :
    if distance[i] == k :
        print(i)
        check = True

if check == False :
    print(-1)





# for i in range(m) :
#     dist.append(list(map(int, input().split())))
#
# def bfs(x) :
#     cnt = 1
#     queue = deque()
#     queue.append(x)
#
#     while queue :
#         x = queue.popleft()
#         for j in range(m) :
#             if x == dist[j][0] :
#                 queue.append(dist[j][1])
        # cnt += 1

        # if cnt == k :
        #     if len(queue) == 0 :
        #         return -1
        #     else :
        #         return queue

# print(bfs(x))